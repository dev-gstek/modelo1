import codecs
from datetime import datetime
from ofxparse import OfxParser
from decimal import Decimal
from django.db import transaction
from .models import BankTransaction

def import_ofx_file(file_path_or_file_object):
    """
    Import an OFX file and create BankTransaction records.
    Returns a tuple of (total_imported, total_skipped_duplicates).
    """
    try:
        if isinstance(file_path_or_file_object, str):
            with codecs.open(file_path_or_file_object, encoding='utf-8', errors='ignore') as f:
                ofx = OfxParser.parse(f)
        else:
            ofx = OfxParser.parse(file_path_or_file_object)
    except Exception as e:
        raise ValueError(f"Failed to parse OFX file: {str(e)}")
        
    account = ofx.account
    statement = account.statement
    
    total_imported = 0
    total_skipped = 0
    
    with transaction.atomic():
        for tx in statement.transactions:
            # tx.id, tx.date, tx.amount, tx.memo
            tx_id = tx.id
            
            if BankTransaction.objects.filter(transaction_id=tx_id).exists():
                total_skipped += 1
                continue
                
            BankTransaction.objects.create(
                transaction_id=tx_id,
                date=tx.date,
                amount=Decimal(str(tx.amount)),
                memo=tx.memo,
                is_reconciled=False
            )
            total_imported += 1
            
    return total_imported, total_skipped

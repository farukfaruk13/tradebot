from flask import Flask, request,
import json
import telebot
from binance.spot import spot as client  

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = json.loads(request.data)
        ticker = data['ticker']
        exchange = data['exchange']
        price = data['price']
        side = data['side']
        quantlity = data['quantity']
        telegramBotApi = data['telegramBotApi']
        telegramUserId = data['telegramUserId']
        binanceApiKey = data['binanceApiKey']
        binanceSecretKey = data['binanceSecretKey']
        params = {
            "symbol" : ticker,
            "side" : side,
            "type" : "MARKET",
            "quantity" : quantlity,
            
        }
        Client(binanceApiKey, binanceSecretKey).new_order(**params)
        telebot.Telebot(telegramBotApi).sendMessage(telegramUserId, 
                                                    f" {ticker} {side}ING on {exchange} \nQuantlity : {quantlity} ")
        
    except :
        pass
        
        return { 
            "code" : "success"
            
            
            
            
            
    
    }

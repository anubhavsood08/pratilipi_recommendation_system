from flask import Flask, request, jsonify
import pandas as pd 

app = Flask(__name__)

recommendations_df = pd.read_csv("recommendations.csv")
@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id',type = int)
    user_recs = recommendations_df[recommendations_df['user_id']== user_id]

    if user_recs.empty:
        return jsonify({"error":"User ID not found"}), 404
    
    recs = user_recs.iloc[0,1:].tolist()
    return jsonify({"user_id": user_id, "recommendations": recs})

if __name__ == '__main__':
    app.run(debug=True,port=5000)
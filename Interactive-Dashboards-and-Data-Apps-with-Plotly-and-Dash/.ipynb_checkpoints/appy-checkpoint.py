{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "changed-coalition",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash is running on http://127.0.0.1:8050/\n",
      "\n",
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\user\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3445: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "import dash\n",
    "import dash_html_components as html\n",
    "\n",
    "#create(instantiate) the app\n",
    "app = dash.Dash(__name__)\n",
    "\n",
    "#app's layout\n",
    "app.layout = html.Div([\n",
    "    html.H1(\"Hello, Kigali!\")\n",
    "])\n",
    "\n",
    "#run the app\n",
    "if __name__=='__main__':\n",
    "    app.run_server(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "induced-yorkshire",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

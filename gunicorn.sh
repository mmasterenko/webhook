source .env

if [[ "$1" == "--reload" ]]; then
  echo "reload gunicorn "
  kill -HUP $(pgrep gunicorn)

elif [[ "$1" == "--stop" ]]; then
  echo "stop gunicorn"
  kill $(pgrep gunicorn)

elif [[ "$1" == "--list" ]]; then
  ps aux | grep gunicorn

else
  echo "start gunicorn"
  gunicorn 'application:app'
fi

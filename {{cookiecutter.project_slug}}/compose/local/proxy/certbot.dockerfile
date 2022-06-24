FROM certbot/certbot
ADD ./compose/local/proxy/letsencrypt-renew /var/spool/cron/crontabs/root

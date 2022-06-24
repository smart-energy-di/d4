FROM certbot/certbot
ADD ./compose/production/proxy/letsencrypt-renew /var/spool/cron/crontabs/root

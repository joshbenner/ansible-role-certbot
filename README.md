# joshbenner.certbot

Install and configure certbot, the official Let's Encrypt client.

## Requirements

* git
* cron (if cronjob enabled)

## Variables

See `defaults/main.yml` for all variables.

Required variables:
* `certbot_account_email`
* `certbot_agree_tos`

## Example Config

```yaml
certbot_account_email: foo@example.com
certbot_version: v0.25.1
certbot_agree_tos: true

certbot_certs:
  - name: main-site
    domains:
      - example.com
      - www.example.com
    method: standalone
  - name: other-site
    domains:
      - other.example.com
    method: dns-route53
    env:
      AWS_ACCESS_KEY_ID: "{{ my_aws_access_key_id }}"
      AWS_SECRET_ACCESS_KEY: "{{ my_aws_secret_key }}"
```

## License

BSD

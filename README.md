# FlyTune Cloud

FlyTune 2.2.3 的公开云端清单与 APK 镜像。客户端只读取公开 JSON，不包含写入令牌。

## 读取链路

1. `https://gitee.com/ebinjfjfjg/flytune-cloud/raw/master/cloud`
2. `https://raw.githubusercontent.com/hz-xb/flytune-cloud/main/cloud`
3. `https://cdn.jsdelivr.net/gh/hz-xb/flytune-cloud@main/cloud`
4. `https://ghproxy.net/https://raw.githubusercontent.com/hz-xb/flytune-cloud/main/cloud`

## 文件

- `cloud/version.json`：版本、APK 地址数组、SHA-256、大小、更新说明。
- `cloud/integrity.json`：当前版本哈希、发布证书 SHA-256、最低允许 versionCode、停用列表。
- `cloud/auth.json`：高级功能授权开关、PBKDF2 参数、盐、密码派生值、有效期。
- `apk/flytune-2.2.3.apk`：签名后的正式安装包。

## 发布新版本

1. 修改 `app/build.gradle.kts` 的 `versionCode` / `versionName`，构建 release APK。
2. 计算 APK 的 SHA-256 与字节数。
3. 把 APK 放到 `apk/`，同步更新 `version.json` 与 `integrity.json`。
4. 推送两个远端；客户端启动时会自动检查。

## 轮换授权密码

```bash
python3 tools/rotate_auth.py '新密码' 2027-12-31
```

脚本只写入 `cloud/auth.json` 的盐与 PBKDF2 派生值，不保存明文密码。

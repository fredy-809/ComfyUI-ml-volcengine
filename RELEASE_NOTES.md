# Release v0.1-beta

发布版本：v0.1-beta (Beta)

发布日期：2025-11-10

简要说明：
- 将当前项目作为 beta 0.1 版本发布的初始包。
- 包含 ComfyUI 的 Doubao-Seed-1.6 自定义节点代码及依赖声明（见 `requirements.txt`）。

主要变更：
- 初始提交：添加自定义节点 `comfy_nodes/doubao_seed_node.py`。
- 补充项目元文件：`LICENSE`、`.gitignore`。

已知问题与限制：
- 目前尚未在 GitHub 上创建远程仓库；下面提供创建并推送到 GitHub 的指导命令（可选使用 `gh` CLI 简化流程）。

部署与发布到 GitHub（推荐步骤）

1. 在本地初始化并提交（如果尚未）并创建标签：
```powershell
# 初始化仓库（若已初始化请跳过）
git init
# 添加文件并提交
git add .
git commit -m "chore: initial commit for v0.1-beta"
# 创建一个带注释的标签
git tag -a v0.1-beta -m "v0.1-beta"
```

2. 在 GitHub 创建远程仓库（两种方式）：
- 使用 Web UI：登录 GitHub，创建新仓库（例如 `doubao-seed-comfyui`），然后将远程添加到本地并推送：
```powershell
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
# 推送标签
git push origin v0.1-beta
```
- 使用 GitHub CLI（已安装并已授权 gh）：
```powershell
gh repo create <your-username>/<repo-name> --public --source=. --remote=origin --push
# 这条命令会把当前分支推到 origin 并创建远程仓库
```

3. 在 GitHub 上创建 Release（可选）：
- 使用 Web UI：进入仓库 -> Releases -> Draft a new release，选择 tag `v0.1-beta`，填写说明并发布。
- 使用 gh CLI：
```powershell
gh release create v0.1-beta --title "v0.1-beta" --notes-file RELEASE_NOTES.md
```

联系方式：
- 作者：Fredy


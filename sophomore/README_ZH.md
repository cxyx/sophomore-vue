


# 4. 权限管理逻辑思考

## 4.1 快速实现菜单权限编辑树
1. 遍历所有没有父菜单的菜单,实现初级主要功能块的区分
2. 根据所有的主菜单遍历下面的

## 4.2 边框菜单的展示控制
1. 遍历所有没有父菜单的`头部菜单`,实现初级主要功能块的区分,生成有序字典
2. 根据1的子菜单且是功能菜单找到所有的子菜单(`框架菜单`,不可点击),填入一级字典的 value
3. 根据 2 的遍历出对应的所有子菜单且是`功能菜单`

```json
{
  "我的工作台":{
    "创建工单": {
      "服务请求单": {
        "url": ""
      }
    }
  } 
}
```


```json

{
  "admin": [
    {
      "path1": "",
      "method":"get"
    },{
      "path2": "",
      "method":"post"
    }
  ]
}
```


# 用户->多角色->多权限

```
celery -A sophomore beat  -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
celery -A sophomore worker -B  -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
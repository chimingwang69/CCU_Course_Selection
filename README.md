# CCU_Course_Selection

### 中正大學搶課程式

待選課系統開放再更新

##### setting.json範例

```json
{
	"wait":1,   //每次發送請求等待時間(單位為秒)
	"stuID": "你的學號",   
	"password": "選課系統密碼",  
	"courseInfo": {
		"隨便你取": {
			"courseID": "課程代碼",
			"courseNum": "班別",
			"deptID": "系所編號",
			"grade": "年級",
			"page": "在加選頁面第幾頁",
			"credit": "學分數",
			"general": 是否為通識課 true/false,
			"cate": "基礎通識填1/博雅通識填2",
			"subcate": "向度"
		},
		"科學飲茶實務": {      //這是個範例
			"courseID": "7500021",  
			"courseNum": "01",
			"deptID": "I001",
			"grade": "1",
			"page": "1",
			"credit": "3",
			"general": true,
			"cate": "2",
			"subcate": "6"
		}
	}
}
```

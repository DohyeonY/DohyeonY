<template>
  <div>
    <b-modal id="modal-center" centered size="lg" hide-footer>
      <!-- 타이틀 -->
      <template #modal-title>
        <h2 style="text-align:center; margin-bottom:30px;"> <b>테마 지도 만들기</b></h2>      </template>

      <!-- 테마 이름 인풋창 -->
      <div class="d-block text-center">
        <h4 style="text-align:left; padding-bottom: 10px;">테마명</h4>
        <v-col style="padding:0px;">
          <v-textarea
            label="ex) 광주 양림동 귀여운 카페"
            auto-grow
            outlined
            maxlength="32"
            rows="1"
            row-height="15"
            v-model="themename"
          ></v-textarea>
        </v-col>
  
              </div>
 
      <!-- 이모지 -->
      <p style="font-size:18px;margin-bottom:8px;"><b>이모지</b></p>  
      <div class="form-item" style="margin-bottom:8px;">
        <input 
        class="input_icon"
        type="text"
        maxlength='6'
        placeholder="ex) 🎄 "
        v-model="themeicon"
        >    
        <span> 
          <button 
          class="Addemoji"  
          onclick="window.open('https://www.emojiengine.com/ko/keyboard/')" > 
          + 이모지
        </button>
        </span>
      </div>
      <br>
      
      <!-- 안내사항 -->
      <h4 style="text-align:left;">테마명 작성과 관련된 안내 사항</h4>
      <div style="padding:10px;">
        <p style="text-align:left">ex) 구체적인 특징이나 상황이 들어간 테마명을 추천해요!</p>
        <li style="text-align:left">예 : 2~3명이 술 마시며 이야기하기 좋은 곳</li>
        <li style="text-align:left">예 : 하루종일 있어도 눈치 보이지 않는 카페</li>
      </div>
      <br>

      <!-- 키워드 -->
      <h4 style="text-align:left; padding-bottom: 10px;">키워드</h4>
      <v-card class="mx-auto">
        <!-- 인원 -->
        <v-card-subtitle style="padding-bottom:0px;">
          <p class="text-h3 text--primary" >
            <b># 인원</b>
          </p>
        </v-card-subtitle>
        <div style="margin-left:20px;">
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px;"
            rounded
            @click="AloneTag"
            >
            🧍 1인
            </v-btn>
          </v-btn-toggle>
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px;"
            rounded
            @click="ManyTag"
            >
            🧑‍🤝‍🧑 다수
            </v-btn>
          </v-btn-toggle>
        </div>
       <!-- 특징 -->

        <v-card-subtitle style="padding-bottom:0px;">
          <p class="text-h3 text--primary" >
            <b># 특징</b>
          </p>
        </v-card-subtitle>
        <div style="margin-left:20px;">
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px; margin-bottom:10px;"
            rounded
            @click="WarmTag"
            >
            🌞 햇살좋은
            </v-btn>
          </v-btn-toggle>
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px; margin-bottom:10px;"
            rounded
            @click="JamTag"
            >
            📢 붐비는
            </v-btn>
          </v-btn-toggle>
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px; margin-bottom:10px;"
            rounded
            @click="CleanTag"
            >
            🧹 깔끔한
            </v-btn>
          </v-btn-toggle>
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px; margin-bottom:10px;"
            rounded
            @click="OldTag"
            >
            👖 빈티지
            </v-btn>
          </v-btn-toggle>
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px; margin-bottom:10px;"
            rounded
            @click="HealthTag"
            >
            💪 건강한
            </v-btn>
          </v-btn-toggle>
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px; margin-bottom:10px;"
            rounded
            @click="InsTag"
            >
            📷 인스타감성
            </v-btn>
          </v-btn-toggle>
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px; margin-bottom:10px;"
            rounded
            @click="ParkTag"
            >
            🚗 주차편한
            </v-btn>
          </v-btn-toggle>
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px; margin-bottom:10px;"
            rounded
            @click="HugeTag"
            >
            🥅 넓은
            </v-btn>
          </v-btn-toggle>
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px; margin-bottom:10px;"
            rounded
            @click="BrightTag"
            >
            💡 밝은
            </v-btn>
          </v-btn-toggle>
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px; margin-bottom:10px;"
            rounded
            @click="DarkTag"
            >
            🔦 어두운
            </v-btn>
          </v-btn-toggle>
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px; margin-bottom:10px;"
            rounded
            @click="TasteTag"
            >
            😋 맛있는
            </v-btn>
          </v-btn-toggle>
          <v-btn-toggle>
            <v-btn
            style="margin-right:10px; margin-bottom:10px;"
            rounded
            @click="CheapTag"
            >
            💰 가성비 좋은
            </v-btn>
          </v-btn-toggle>
        </div>
        <br>
      </v-card>

      <br>
      <!-- 미리보기 -->
      <p style="font-size:18px;"><b>미리보기</b></p>
      <div class="theme_preview">
        <div class="iconbox">
          <p class="themeicon">{{themeicon}}</p>
        </div>
        <!-- 제목 박스 -->
        <div class="namebox">
          <p class="themename"><b>{{themename}}</b></p>
        </div>
        <!-- 하위 정보  -->
        <div class="bottombox">
          <p style="font-size:14px;text-align:center;margin-bottom:1px;"> ㅇㅇㅇ님</p>
          <div class="infobox" style="margin:auto;">
            <div style="text-align:center;">
              <!-- 큐레이터 명수 -->
              <span style="font-size:12px;text-align:center;color:grey;margin:a;"> 🧑🏻‍🤝‍🧑🏻 6명</span> 
              <!-- 장소 -->
              <span style="font-size:12px;text-align:center;color:grey;"> <b>｜</b>🏡 10개 </span>
            </div>
          </div>
        </div>
      </div>
      <br>
      <!-- 저장하기 버튼 -->
      <b-button class="mt-3" block style="display:block; margin:auto;" @click="CreateThema">저장하기</b-button>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
// import router from '@/router'

export default {
  name : 'ThemaCreateModal',
  data () {
    return {
      themename:'',
      themeicon:'',
      theme_tags: [],

    }
  },
  methods : {
    CreateThema () {
      console.log(123)
      const theme_title = this.themename
      const imoge = this.themeicon
      const theme_tags = this.theme_tags
      const theme_creator = '테스트'
      axios({
        method: 'post',
        url: `http://localhost:8000/api/v1/themes/create/`,
        data: {
          theme_title,
          imoge,
          theme_creator,
          theme_tags
        }
      })
      .then((res) => {
        console.log('then123')
        console.log(res.data)
        console.log(this.theme_tags)
        // router.go(0)
        
      })
      .catch((err) => {
        console.log('catch123')
        console.log(err)
      })
    },

    // 태그 저장 이벤트들
    AloneTag () {
      if (this.theme_tags.includes('53') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '53'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('53')
      }
      console.log(this.theme_tags)
    },
    ManyTag () {
      if (this.theme_tags.includes('54') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '54'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('54')
      }
      console.log(this.theme_tags)
    },
    WarmTag () {
      if (this.theme_tags.includes('55') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '55'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('55')
      }
      console.log(this.theme_tags)
    },
    JamTag () {
      if (this.theme_tags.includes('56') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '56'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('56')
      }
      console.log(this.theme_tags)
    },
    CleanTag () {
      if (this.theme_tags.includes('57') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '57'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('57')
      }
      console.log(this.theme_tags)
    },
    OldTag () {
      if (this.theme_tags.includes('58') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '58'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('58')
      }
      console.log(this.theme_tags)
    },
    InsTag () {
      if (this.theme_tags.includes('59') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '59'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('59')
      }
      console.log(this.theme_tags)
    },
    HealthTag () {
      if (this.theme_tags.includes('60') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '60'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('60')
      }
      console.log(this.theme_tags)
    },
    ParkTag () {
      if (this.theme_tags.includes('61') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '61'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('61')
      }
      console.log(this.theme_tags)
    },
    HugeTag () {
      if (this.theme_tags.includes('62') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '62'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('62')
      }
      console.log(this.theme_tags)
    },
    TasteTag () {
      if (this.theme_tags.includes('63') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '63'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('63')
      }
      console.log(this.theme_tags)
    },
    BrightTag () {
      if (this.theme_tags.includes('64') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '64'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('64')
      }
      console.log(this.theme_tags)
    },
    DarkTag () {
      if (this.theme_tags.includes('65') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '65'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('65')
      }
      console.log(this.theme_tags)
    },
    CheapTag () {
      if (this.theme_tags.includes('66') === true) {
        console.log('if문 통과')
        this.theme_tags = this.theme_tags.filter(function(item) {
          return item !== '66'
        })
      } else {
        console.log('else문 통과')
        this.theme_tags.push('66')
      }
      console.log(this.theme_tags)
    },

  },
}
</script>

<style scoped>
#modal_content{
  font-family:"Pretendard-Regular";
  color:black;
}
/* 테마명 작성 */
.input_themename{
  width:350px;
  height:45px;
  border: 1px solid #969696;
  padding:10px;
  font-size:14px;
}
.form-item input:focus{
  border:none;
  outline:1px solid #f68335;
}

.input_icon{
  width:350px;
  height:45px;
  border: 1px solid #969696;
  padding:10px;
  font-size:14px;
}
input::placeholder {
  color: #969696;
  font-size:14px;
}

/* 아이콘 */
.Addemoji{
  text-align: center;
  width:70px;
  height: 30px;
  border: 2px solid lightgrey;
  color:gray;
  border-radius: 50px;
  font-size:12px;
}
.Addemoji:hover{
  text-align: center;
  width:70px;
  height: 30px;
  border:none;
  border: 2px solid rgb(49, 49, 49);
  color:rgb(31, 31, 31);
  border-radius: 50px;
  font-size:12px;
  font-weight: 700;
}
/* 미리보기 */
.theme_preview{
  width:300px;
  height: 165px;
  border: 2px solid lightgrey;
  border-radius: 50px;
  margin:auto;
  box-shadow: 1px 1px 10px #969696;
}
.themeicon{
  text-align: center;
  font-size:17px;
  padding:5px;
}
.iconbox{
  height: 25px;
  margin-top:10px;
}
.themename{
  font-size:15px;
}
.namebox{
  width:200px;
  height: 55px;
  margin:auto;
  margin-top:10px;
  text-align: center;
  padding:5px;
}
/* 생성 */
.Addbutton{
  width:120px;
  height:35px;
  color:white;
  background-color: #9a09d3;
  border-radius: 20px;
  margin-top:20px;
  margin-left: 40%;

}
@font-face {
    font-family: 'Pretendard-Regular';
    src: url('https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
    font-weight: 400;
    font-style: normal;
}

.add-place-page{
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	font-size:13px
}
.header{
	text-align: center;
}
.body{
	height: 80%;
	overflow: auto;
	background-color:#f8f9fa;
	font-size:13px;
}
.footer{
	text-align: center;	
}
.category-box{
	display: flex;
	align-items: center;
	justify-content: space-evenly;
}
.category-item{
	box-shadow: 1px 1px 4px rgb(0 0 0 / 20%);
	border-radius: 5px;
	width:25%;
	height: 40px;
	display: flex;
	cursor: pointer;
}
.category-item > span{
	margin:auto
}
.category-item:hover{
	background-color: skyblue;
	color:aliceblue
}

.submit-category-tag{
	border:none;
	width:80%;
	cursor: pointer;
	font-size:16px;
	border-radius: 5px;
	padding: 10px;
	background-color: #FFA0A0;
	color: white;
	font-weight: bold;
}
.submit-category-tag:hover{
	background-color: #FFC6C6;
}

.selected{
	background-color: skyblue;
	color:aliceblue
}

::-webkit-scrollbar {
  display: none;
}


</style>

<style>
.page2-header-para{
	font-size:17px;
	font-weight: bold;
	margin-bottom:10px;
	text-align: center;
}
</style>
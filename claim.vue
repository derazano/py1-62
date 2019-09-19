<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <v-list-item @click="null">
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click="null">
          <v-list-item-action>
            <v-icon>mdi-contact-mail</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Contact</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="blue"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>แบบเรียกร้องค่าสินไหมทดแทนค่ารักษาพยาบาล</v-toolbar-title>
    </v-app-bar>
  
    <v-container  class="justify-center">
      <v-layout  row nowrap class="justify-center">
        <v-flex md12 xs12 lg12 xl3>
              <v-col>
              <h3 class="text-center">
                      รายละเอียดการรักษาพยาบาล
              </h3>
              </v-col>
        </v-flex>  
              <v-flex md6 xs12 lg4 xl3>
                  <v-text-field
                      class="justify-center"
                      label="Regular"
                      style="width:300px"
                  ></v-text-field>
              </v-flex>
              <v-flex md6 xs12 lg4 xl3>
                  <v-btn @click="findCustomer" depressed large color="primary">Search</v-btn>
              </v-flex>
               <v-flex md6 xs12 lg4 xl3>
                  <v-select
                    style="width: 300px"
                    label="ให้สั่งจ่ายเช็คในนามของ"
                    v-model="claim.paychecksId"
                    :items="paychecks"
                    item-text="payto"
                    item-value="id"
                    :rules="[(v) => !!v || 'Item is required']"
                  ></v-select>
               </v-flex>
       
               
                 <v-select
                  style="width: 300px"
                    label="ได้รับการตรวจตามวิธีการต่อไปนี้หรือไม่"
                    v-model="claim.treatMethodId"
                    :item="treatMethod"
                    item-text="treatby"
                    item-value="id"
                    :rules="[(v) => !!v || 'Item is required']"
                  ></v-select>
          
         
                 <v-select
                  style="width: 300px"
                    label="ได้รับการรักษาโดยวิธีการ"
                    v-model="claim.curebyId"
                    :item="cureby"
                    item-text="curemeth"
                    item-value="id"
                    :rules="[(v) => !!v || 'Item is required']"
                  ></v-select>
             
                  <v-select
                  style="width: 300px"
                    label="แพคเก็จที่สมัครกับเรา"
                    v-model="claim.insurancetypeId"
                    :item="insurancetype"
                    item-text="id"
                    item-value="id"
                    :rules="[(v) => !!v || 'Item is required']"
                  ></v-select>
              
                  <v-select
                  style="width: 300px"
                    label="ชื่อโรงพยาบาล"
                    v-model="claim.branchId"
                    :item="branch"
                    item-text="name"
                    item-value="id"
                    :rules="[(v) => !!v || 'Item is required']"
                  ></v-select>
     </v-layout>
     
           
           
    </v-container>
            <div class="btncenter">
            <v-col cols="12">
              <v-btn large class="justify-center" md4 style="hight:300" depressed color="primary">ส่งแบบฟอร์ม</v-btn>  
            </v-col>
            </div>
  </v-app>
</template>

<script>
import http from "../Api";
  export default {
    name: "claim",
    props: {
      source: String,
    },
   data() {
    return {
      claim: {
        paychecksId: "",
        treatmethodId: "",
        branchId: "",
        insurancetypeId:"",
        curebyId:""
      },
      valid: false,
      customerCheck: false,
      customerName: "",
      drawer: false
    };
  },
  methods:{
   /* eslint-disable */
    getPaychecks(){
      http
      .get("/paychecks")
      .then(response =>{
        this.paychecks = response.data;
        console.log(response.data);
      })
      .catch(e =>{
        console.log(e);
      });
    },
    getTreatMethod(){
      http
      .get("/treatmethod")
      .then(response =>{
        this.treatmethod = response.data;
        console.log(response.data);
      })
      .catch(e =>{
        console.log(e);
      })
    },
    getBranch(){
      http
      .get("/branch")
      .then(response =>{
        this.branch = response.data;
        console.log(response.data);
      })
      .catch(e=>{
        console.log(e);
      })
    },
    getInsurancetype(){
      http
      .get("/Insurancetype")
      .then(response =>{
        this.insurancetype = response.data;
        console.log(response.data);
      })
      .catch(e=>{
        console.log(e);
      })
    }
  },
 mounted() {
 this.getPaychecks();
 this.getTreatMethod();
 this.getBranch();
 this.getInsurancetype();
 }

  };

</script>

<style>
.btncenter{
    
    display: block;
    margin-left: auto;
    margin-right: auto;
}
</style>

<template>
  <div>
    <h1>Booking</h1>
    <div class="booking">
      <form action="">

        <div class="content">
          <label>Name:</label> 
          <input type="text" name="FullName" v-model='name'/>
        </div>

        <div class="content">
          <label>E-mail:</label>
          <input type="text" name="Email" v-model='email'/>
        </div>
        
        <div class="gender"> 
          <label>Gender:
            <input id="male" type="radio" name="Sex" value="m" />
            <label for="male">男</label>
            <input id="female" type="radio" name="Sex" value="f" />
            <label for="female">女</label>
          </label>
        </div>

        <div class="content">
          <label>Tel:</label>
          <input type="text" name="Phone" v-model='tel'>
        </div>

        <div class="content">
          <label>booking-times:</label> 
          <input type="datetime-local" name="Times" v-model='time'>
        </div>

        <div class="content">
          <label>courses:</label> 
          <select v-model='course'>
              <option value="0">select</option>
              <option v-for="course in coursesName" :value="course.id">
                {{course.name}}
              </option>
          </select>
        </div>

        <div>
          <button class="submit">submit</button>
        </div>
        
      </form>
    </div>
  </div>
 
  
</template>

<script>
import courses from './courses';

export default {
  data(){
    return {
      name:'',
      tel: '',
      time: '',
      course: 0,
      email: '',
    };
  },
  computed:{
    coursesName(){
      return courses;
    },
  },
};
</script>

<style scoped>
  form {
    margin: 20px;
    width:600px;
  }

  h1 {
    margin-left: 560px;
    font-size: 36px;
  }
  .booking {
    display: flex;
    justify-content: center;
    height: 560px;
  }

  label {
    display: inline-block;
    padding-bottom: 6px;
    font-size: 24px;
  }

  .content {
    margin-bottom: 0.5em;
  }

  .content > input {
    width: 100%;
    display: flex;
    font-size: 24px;
  }

  .content > select {
    width: 100%;
    display: flex;
    font-size: 24px;
  }

  .gender > label > input {
    width: 20px;
    height: 20px;
  }

  .submit {
    color: white;
    background: black;
    border-radius: 5px solid;
    padding: 8px 12px;
    font-size: 20px;
    margin-top: 14px;
    float: right ;
    border-radius: 10px;
  }


</style>
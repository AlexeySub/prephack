<template>

  <div class="container">
    <div class="row">
      <div class="col-md-5 mx-auto">
    <h1>Форма регистрации</h1>

    <form>

      <div v-show="visible" class="form-group derror">
      <b>Пожалуйста исправьте указанные ошибки:</b>
        <p v-for="error in errors">{{ error }}</p>
      </div>

    <div class="form-group">
      <input  v-model="login" type="text" placeholder="Логин" name="uname" required>
    </div>

      <div class="form-group">
      <input  v-model="email" type="email" placeholder="Почта" name="uname" required>
      </div>

      <div class="form-group">
      <input  v-model="password" type="password" placeholder="Введите пароль" name="psw" required>
      </div>

      <div class="form-group">
      <input  v-model="passwordb" type="password" placeholder="Повторите пароль" name="psw" required>
      </div>

      <div class="form-group ">
        <b-form-group>
          <b-form-radio-group
            id="btn-radios-1"
            v-model="selected"
            :options="options"
            buttons
            label="Material unchecked"
          color ="info"
            name="radios-btn-default"
          ></b-form-radio-group>
        </b-form-group>
      </div>

      <div class="form-group">
        <button @click="fregistr" type="button" class="btn btn-secondary">Зарегистрироваться</button>
      </div>

    </form>
      </div>
    </div>

  </div>

</template>

<script>
    export default {
      name: "Registr",
      data() {
        return {
          login: "",
          password: "",
          email: "",
          passwordb: "",
          selected: "",
          errors: [],
          visible: false,
          options: [
            { text: 'Я студент', value: 'ST' },
            { text: 'Я учитель', value: 'TC' }],
        }
      },
      methods: {
        fregistr: function (e) {
          e.preventDefault();

          if (this.login && this.password && this.email && this.passwordb && this.selected) {
            console.log(this.selected);
            axios.post('/users/', {
              username: this.login,
              password: this.password,
              usertype: this.selected,
              email: this.email
            })
              .then(function (response) {

                console.log(response);
              })
              .catch(function (error) {


                console.log(error);
              });


            this.$router.push({name: "login"});
          }
          else {
            this.visible=!this.visible;
            this.errors.push('Заполните все поля!');

          }


        }
      }

    }
</script>

<style scoped>

  .btn-secondary:not(:disabled):not(.disabled):active, .btn-secondary:not(:disabled):not(.disabled).active, .show > .btn-secondary.dropdown-toggle {
    color: #fff;
    background-color: #0080ff !important;
    border-color: #4e555b !important;
  }

  .derror {
    color: brown;
  }

  .container {
    text-align: center;
    margin-top: 50px;
  }

  .btn {
    background-color: #6c757d;
    border-radius: 5px;
    color: white;
  }

  .btn-secondary:not(:disabled):not(.disabled).active, .btn-secondary:not(:disabled):not(.disabled):active, .show>.btn-secondary.dropdown-toggle {
    color: #fff;
    background-color: #6c757d;
    border-color: #6c757d;;
  }



</style>

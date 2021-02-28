<template>
    <article>
        <section>
            <button @click="buttonClicked(0)" id="button0" class="button-layout"></button>
            
            <button @click="buttonClicked(3)" id="button3" class="button-layout"></button>
            <button @click="buttonClicked(6)" id="button6" class="button-layout"></button>
        </section>
        <section>
            <button @click="buttonClicked(1)" id="button1" class="button-layout"></button>
            <button @click="buttonClicked(4)" id="button4" class="button-layout"></button>
            <button @click="buttonClicked(7)" id="button7" class="button-layout"></button>
        </section>
        <section>
            <button @click="buttonClicked(2)" id="button2" class="button-layout"></button>
            <button @click="buttonClicked(5)" id="button5" class="button-layout"></button>
            <button @click="buttonClicked(8)" id="button8" class="button-layout"></button>
        </section>
    </article>
</template>

<script>
    export default {
        data(){
            return {
                playerOneTurn: true,
                playerOneTurnList: [],
                playerTwoTurnList: [],
                winning_positions: [
                    [1,3,5],
                    [1,2,3],
                    [3,6,9],
                    [1,5,9],
                    [7,8,9],
                    [3,5,7],
                    [2,5,8],
                    [4,5,6]
                ]
            }
        },
        methods:{
            buttonClicked: function(buttonNumber){
                console.log(buttonNumber);
                if (this.playerOneTurn){
                    const button = document.getElementById(`button${buttonNumber}`)
                    button.textContent = 'X'
                    this.addButtonToPlayerList(true, buttonNumber)
/                } else if (!this.playerOneTurn){
                    const button = document.getElementById(`button${buttonNumber}`)
                    button.textContent = 'O'
                }
                this.playerOneTurn =  !this.playerOneTurn
/            },
            checkForWin: function(){

            },
            addButtonToPlayerList: function(playerTurn, buttonNumber){
                if (this.playerOneTurn){
                    this.playerOneTurnList.push(buttonNumber+1)
                } else{
                    this.playerTwoTurnList.push(buttonNumber+1)
                }
            }
        }
        
    }
</script>

<style lang="css" scoped>

.button-layout{
    display: block;
    height: 100px;
    width: 100px;
    font-size: xx-large;
    padding: 10px;
    margin: 10px;
}

h1{
    margin: 0px;
}

article{
    display: flex;
    flex-wrap: wrap ;
}

</style>
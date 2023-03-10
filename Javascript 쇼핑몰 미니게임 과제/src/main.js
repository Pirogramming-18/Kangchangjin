
//fetch the items from the JSON file
function loadItems(){
    return fetch('data/data.json')
    .then(response=>response.json())
    .then(json=>json.items);
}
//updatae the list with the given items
function displayItems(items){
    const container=document.querySelector('.items');
    container.innerHTML=items.map(item=>createHTMLString(item)).join('');

}
//create HTML list item from the given item
function createHTMLString(item){
    return `
    <li class="item">
    <img src="${item.image}" alt="${item.type}" class="item_thumbnail">
    <span class="item_description">${item.gender}, ${item.size}</span>
    </li>
    `;
}
function onButtonClick(e,items){
    const dataset=e.target.dataset;
    const key=dataset.key;
    const value=dataset.value;
    
    if(key==null||value==null){
        return;
    }
    // displayItems(items.filter(item=>item[key]===value))
    updateItems(items,key,value);
}

function updateItems(items,key,value){
    items.forEach(items => {
        if(item.datset[key]===value){
            item.classList.remove('invisible');
        }
        else{
            item.classList.add('invisible');
        }
    });
}

function setEventListeners(items){
    const logo=document.querySelector('.logo');
    const buttons=document.querySelector('.buttons');
    logo.addEventListener('click',()=>displayItems(items));
    buttons.addEventListener('click',Event=>onButtonClick(e,items));

}
//main
loadItems()
    .then(items=>{
        displayItems(items);
        setEventListeners(items);
    })
    .catch(console.log);
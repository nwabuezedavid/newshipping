


let por = location.protocol
async function datgetfetching() {
    urlx = location.host
    const divs = document.querySelector('#contesf')
    let d = await fetch(`${por}//${urlx}/fetch/`)
    let dd = await d.json()
    dd.data.forEach(e => {
        

        divs.innerHTML +=`<div id="id${e.uuid}" class="xl:w-1/4 md:w-1/2 p-4">
  <div class="bg-white shadow-md hover:shadow-lg p-6 rounded-lg text-sm border border-gray-200 transition-shadow duration-300">
    <h3 class="tracking-widest text-red-600 text-xs font-medium title-font mb-4 uppercase">
      Refcode: ${e.uuid}
    </h3>

    <ul class="leading-relaxed text-gray-700 text-base w-fit flex flex-col gap-2 mb-4">
      <li><strong>Sender:</strong> ${e.SName}</li>
      <li><strong>Recipient:</strong> ${e.RName}</li>
      <li><strong>Phone:</strong> ${e.RPhone}</li>
      <li><strong>From:</strong> ${e.Origin}</li>
      <li><strong>To:</strong> ${e.Destination}</li>
      <li class="w-full word-wrap" ><strong>Recipient Email:</strong> ${e.REmail}</li>
      <li class="w-full word-wrap" ><strong class="w-full word-wrap"  >Sender Email:</strong> ${e.SEmail}</li>
      <li><strong>Mode:</strong> ${e.Mode}</li>
      <li><strong>Amount:</strong> ${e.Amount}</li>
    </ul>

    <div class="flex flex-wrap gap-2">
      <a 
        class="p-2 px-4 bg-blue-500 text-white rounded hover:bg-blue-600 cursor-pointer transition-colors duration-200"
        onclick="toggleds('#updatehistory'), locad('${e.uuid}')"
      >
        Add History
      </a>
      <a 
        class="p-2 px-4 bg-green-500 text-white rounded hover:bg-green-600 cursor-pointer transition-colors duration-200"
        onclick="toggledsput('#createas', '${e.uuid}'), locad('${e.uuid}')"
      >
        Edit
      </a>
      <a 
        class="p-2 px-4 bg-red-500 text-white rounded hover:bg-red-600 cursor-pointer transition-colors duration-200"
        onclick="allto('#id${e.uuid}'), Deletea('${e.uuid}')"
      >
        Delete
      </a>
      <a 
        href="../../TRACKINGRESULT/${e.uuid}"
        class="p-2 px-4 bg-gray-500 text-white rounded hover:bg-gray-600 cursor-pointer transition-colors duration-200"
      >
        View
      </a>
      <a 
        href="../../Print/${e.uuid}"
        class="p-2 px-4 bg-gray-500 text-white rounded hover:bg-gray-600 cursor-pointer transition-colors duration-200"
      >
        Print
      </a>
    </div>
  </div>
</div>

`

    });
   






   
    
}
datgetfetching()
function datfetchingone(pk) {
 const Locationx = document.querySelector('#Location')
    const Status = document.querySelector('#Status')
    const Remarks = document.querySelector('#Remarks')
    const datetimec = document.querySelector('#datetimec')
   
   
   
    const csrf = document.querySelector('#csrfsd')
 urlx = location.host

    fetch(`${por}//${urlx}/fetchone/${pk}/`,
    {
      method:"PATCH",
    
      headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrf.value
      },
      body:JSON.stringify({
        
         Location :Locationx.value,
         Status :Status.value,
         datetimec :datetimec.value,
        Remarks :Remarks.value, 
        })
    }
    ).catch(err=> alert("soory 404 erro"))

    Locationx.value = ""
    Status.value = ""
    datetimec.value = ""
    Remarks.value = ""
    toggleds('#updatehistory')
    alert('create')
    
}
  function datfetching(data) {


      const SName = document.querySelector('#SName')
      const SAddress = document.querySelector('#SAddress')
      const SEmail = document.querySelector('#SEmail')
      const SPhone = document.querySelector('#SPhone')
      const message = document.querySelector('#message')
      const RName = document.querySelector('#RName')
      const RAddress = document.querySelector('#RAddress')
      const REmail = document.querySelector('#REmail')
      const RPhone = document.querySelector('#RPhone')
      const Origin = document.querySelector('#Origin')
      const Destination = document.querySelector('#Destination')
      const Mode = document.querySelector('#Mode')
      const Quantity = document.querySelector('#Quantity')
      const Weight = document.querySelector('#Weight')
      const Amount = document.querySelector('#Amount')
      const PaymentMode = document.querySelector('#PaymentMode')
      const Delivery = document.querySelector('#Delivery')
      const DepartureDate = document.querySelector('#DepartureDate')
      const PackageItems = document.querySelector('#PackageItems')
      const messagex = document.querySelector('#message')
    
      
      if (
        !SName.value || !SAddress.value || !SEmail.value || !SPhone.value 
    ) {
        alert("Please fill in all fields before submitting.");
        return; // Stop the function if validation fails
    }
      const csrf = document.querySelector('#csrfsd')
  urlx = location.host

      fetch(`${por}//${urlx}/fetch/`,
      {
        method:data,
      
        headers:{
          'Content-Type':'application/json',
          'X-CSRFToken':csrf.value
        },
        body:JSON.stringify({
          


    SName :      SName.value,
    SAddress : SAddress.value,
    SEmail : SEmail.value,
    SPhone : SPhone.value,
    message : message.value,
    RName : RName.value,
    RAddress : RAddress.value,
    REmail : REmail.value,
    RPhone : RPhone.value,
    Origin : Origin.value,
    Destination : Destination.value,
    Mode : Mode.value,
    Quantity : Quantity.value,
    Weight : Weight.value,
    Amount : Amount.value,
    PaymentMode : PaymentMode.value,
    Delivery : Delivery.value,
    DepartureDate : DepartureDate.value,
    PackageItems : PackageItems.value,
    
    
    
  
    message : messagex.value,
        })
      }
      )
      .then(e=> e.json())
      .then(d => {
        location.reload()
        localStorage.clear()
      })
      .catch(s => allmessage("an error occurred "))
      
  }
function datfetchingupdate(data, pk) {

try {
  

    const SName = document.querySelector('#SName')
    const SAddress = document.querySelector('#SAddress')
    const SEmail = document.querySelector('#SEmail')
    const SPhone = document.querySelector('#SPhone')
    const message = document.querySelector('#message')
    const RName = document.querySelector('#RName')
    const RAddress = document.querySelector('#RAddress')
    const REmail = document.querySelector('#REmail')
    const RPhone = document.querySelector('#RPhone')
    const Origin = document.querySelector('#Origin')
    const Destination = document.querySelector('#Destination')
    const Mode = document.querySelector('#Mode')
    const Quantity = document.querySelector('#Quantity')
    const Weight = document.querySelector('#Weight')
    const Amount = document.querySelector('#Amount')
    const PaymentMode = document.querySelector('#PaymentMode')
    const Delivery = document.querySelector('#Delivery')
    const DepartureDate = document.querySelector('#DepartureDate')
    const PackageItems = document.querySelector('#PackageItems')
    
     const csrf = document.querySelector('#csrfsd')
  urlx = location.host
    const messagex = document.querySelector('#message')
   
  console.log(pk);
  

    fetch(`${por}//${urlx}/fetchone/${pk}/`,
    {
      method:data,
    
      headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrf.value
      },
      body:JSON.stringify({
        


  SName :      SName.value,
  SAddress : SAddress.value,
  SEmail : SEmail.value,
  SPhone : SPhone.value,
  message : message.value,
  RName : RName.value,
  RAddress : RAddress.value,
  REmail : REmail.value,
  RPhone : RPhone.value,
  Origin : Origin.value,
  Destination : Destination.value,
  Mode : Mode.value,
  Quantity : Quantity.value,
  Weight : Weight.value,
  Amount : Amount.value,
  PaymentMode : PaymentMode.value,
  Delivery : Delivery.value,
  DepartureDate : DepartureDate.value,
  PackageItems : PackageItems.value,
  Location :Location.value,
  Status :Status.value,
  Remarks :Remarks.value,
  
  
 
  message : messagex.value,
      })
    }
    )
    toggleds('#createas')
    
    localStorage.clear()
  } catch (error) {
    setTimeout(() => {
      
      allmessage('sorry an error occurred')
    }, 2000);
  
  }
    
}
function locad(ds) {
    localStorage.setItem('update', ds)
    
    
}

const addhistory = document.querySelector('#addhistory')
addhistory.addEventListener('submit', (e)=>{
    e.preventDefault()
    datfetchingone(localStorage.getItem('update'))
    // localStorage.removeItem('update')
    
})
const crwate = document.querySelector('#creates_S')
crwate.addEventListener('submit', (e)=>{
    e.preventDefault()
    if (localStorage.getItem('request') == "PUT") {
      
        localStorage.getItem('update')
        
        datfetchingupdate("PUT", localStorage.getItem('update'))
        localStorage.removeItem('request')
        localStorage.clear()

    } else {
        
        datfetching("POST") 
    }
  
})


function toggleds(data) {
    let cs = document.querySelector(data)
    cs.classList.toggle('hidden')
    if (cs.classList.contains('hidden')  ){
      localStorage.clear()
          }
        else{
            
      
           document.querySelector('#SName').value = ''
           document.querySelector('#SAddress').value = ''
             document.querySelector('#SEmail').value =""
             
             document.querySelector('#SPhone').value =""
             
               document.querySelector('#message').value =""
             
                document.querySelector('#RName').value =""
             
                document.querySelector('#RAddress').value =""
             
               document.querySelector('#REmail').value =""
             
                 document.querySelector('#RPhone').value =""
             
               document.querySelector('#Origin').value =""
             
               document.querySelector('#Destination').value =""
             
              document.querySelector('#Mode').value =""
              document.querySelector('#Quantity').value =""
              
              document.querySelector('#Weight').value =""
             
                  document.querySelector('#Amount').value =""
             
               document.querySelector('#PaymentMode').value =""
             
              document.querySelector('#Delivery').value =""
            
                  
            document.querySelector('#DepartureDate').value =""
            
           
        document.querySelector('#PackageItems').value =""
        
        
          }
    
}
function toggledsput( data,datamd) {
    let cs = document.querySelector(data)
    cs.classList.toggle('hidden')
    urlx = location.host
    if (cs.classList.contains('hidden')  ){
      localStorage.clear()
      

     document.querySelector('#SName').value = ''
     document.querySelector('#SAddress').value = ''
       document.querySelector('#SEmail').value =""
       
       document.querySelector('#SPhone').value =""
       
         document.querySelector('#message').value =""
       
          document.querySelector('#RName').value =""
       
          document.querySelector('#RAddress').value =""
       
         document.querySelector('#REmail').value =""
       
           document.querySelector('#RPhone').value =""
       
         document.querySelector('#Origin').value =""
       
         document.querySelector('#Destination').value =""
       
        document.querySelector('#Mode').value =""
        document.querySelector('#Quantity').value =""
        
        document.querySelector('#Weight').value =""
       
            document.querySelector('#Amount').value =""
       
         document.querySelector('#PaymentMode').value =""
       
        document.querySelector('#Delivery').value =""
      
            
      document.querySelector('#DepartureDate').value =""
      
     
  document.querySelector('#PackageItems').value =""
  
  
    }else{
            localStorage.setItem('request', "PUT")
         
    const messagex = document.querySelector('#message')
    fetch(`${por}//${urlx}/fetchone/${datamd}/`)

    .then(res=>res.json())
    .then((data)=>{
        console.log(data);
        

     document.querySelector('#SName').value = data.SName
   document.querySelector('#SAddress').value = data.SAddress
     document.querySelector('#SEmail').value = data.SEmail
     document.querySelector('#SPhone').value = data.SPhone
      document.querySelector('#message').value = data.message
     document.querySelector('#RName').value = data.RName
      document.querySelector('#RAddress').value = data.RAddress
     document.querySelector('#REmail').value = data.REmail
     document.querySelector('#RPhone').value = data.RPhone
     document.querySelector('#Origin').value = data.Origin
    document.querySelector('#Destination').value = data.Destination
    document.querySelector('#Mode').value = data.Mode 
      document.querySelector('#Quantity').value = data.Quantity
     document.querySelector('#Weight').value = data.Weight 
     document.querySelector('#Amount').value = data.Amount
    document.querySelector('#PaymentMode').value = data.PaymentMode
    document.querySelector('#Delivery').value =data.Delivery
    document.querySelector('#DepartureDate').value =data.DepartureDate
document.querySelector('#PackageItems').value = data.PackageItems
    }) }
    
  }
  
  
  function allto( data) {
    let cs = document.querySelector(data)
    cs.classList.toggle('hidden')
  }
  function allmessage(c) {
    document.innerHTML +=`
    <div>
    <div onclick="this.style.display ='none'" class=" fixed top-2  flex left-2 w-full bg-green-100 border-l-4 border-green-500 text-green-700 p-4" role="alert">
    <p class="font-bold"${c}</p>
     
  </div>
 </div>`
}

function Deletea(pk) {
  urlx = location.host
  
     const csrf = document.querySelector('#csrfsd')
 
  fetch(`${por}//127.0.0.1:8000/fetchone/${pk}`,{
    method:'DELETE',
     headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrf.value
      },
  }).then(res=>res.json())
  .then(data => console.log(data))
  
  
  
}
function Deleteall() {
  urlx = location.host
  fetch(`${por}//${urlx}/fetch/`,{method:'DELETE'})
  
    
}
localStorage.clear()
 # simple frame system
 
 module DMAP
   class Frame
     attr_accessor :name
     attr_accessor :abstractions
     attr_accessor :specializations
     attr_accessor :all_abstractions
     attr_accessor :features
      
     def initialize name, parents=[], features=[]
       @name = name
       @abstractions = parents
       @features = features
     end
     
     def parents
       @abstractions
     end    
   end
      
   class Memory
     def initialize
       @m = Hash.new
     end
     
     def clear
       @m.clear
     end
     
     def size
       @m.size
     end
     
     def frame name, parents=[], features=[] 
       @m[name.to_sym] = Frame.new name, parents, features
     end
     
     def parents name
       f = @m[name.to_sym]
       f ? f.parents : []
     end
     
     def frame_of name
       @m[name] || false  # Error?
     end
     
     def frame? o
       o.class==Frame ? true : ((@m[o.to_sym] && true) || false)
     end
     
     def name o
       o.class==Frame ? o.name : o
     end
     
     def force_frame name
       @m[name] || frame(name)
     end
     
   end
 end
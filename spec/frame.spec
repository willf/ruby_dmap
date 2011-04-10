require File.dirname(__FILE__) + '/test_helper'

describe "Simple Frame System"  do
  it 'should be able to create a Memory instance' do
    lambda do                 
      Memory.new
    end.should_not raise_error
  end
  
  it 'should be able to create a Fream inside a Memory' do
    lambda do                 
      m = Memory.new 
      m.frame :root
    end.should_not raise_error
  end
  
  it 'should allow size queries' do
    m = Memory.new
    m.size.should == 0
    m.frame :m_root
    m.size.should == 1
  end
  
  it 'should allow the creation of Frame abstractions' do 
    m = Memory.new
    m.frame :m_root
    m.frame :m_child, [:m_root]
    m.parents(:m_child).should == [:m_root]
  end 
   
  it "should allow testing for frame existence (false)" do
    m = Memory.new
    m.frame?(:m_root).should == false
  end
  
  it 'should allow testing for frame existence (true)' do
    m = Memory.new
    m.frame :m_root
    m.frame?(:m_root).should == true
  end 
  
  it 'should find the naem of objects in the system' do
    m = Memory.new
    m.frame :m_root
    m.name(:m_root).should == :m_root
  end
  
  it 'should allow things to name themselves' do
    m = Memory.new
    m.name(42).should == 42
  end
  
  it 'should allow one to force something to be a frame' do 
    m = Memory.new
    m.force_frame :m_root
    m.frame_of(:m_root).name.should == :m_root
  end
  
end
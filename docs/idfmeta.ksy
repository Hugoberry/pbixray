meta:
  id: idfmeta_parser
  file-extension: idfmeta
  endian: le
  license: CC0-1.0
  title: Column Data Storage Metadata
seq:
  - id: blocks
    type: block

types:
  block:
    seq:
      - id: cp
        type: c_p_element
        
      - id: sdos
        type: s_d_os_element
  
  c_p_element:
    seq:
      - id: cp_tag
        contents: ['<1:CP',0x00]
        
      - id: version_one
        type: u8

      - id: cs
        type: c_s0_element
        
      - id: cp_tag_end
        contents: ['CP:1>',0x00]

  c_s0_element:
    seq:
      - id: cs_tag
        contents: ['<1:CS',0x00]
      
      - id: records
        type: u8
        
      - id: one
        type: u8
      
      - id: a_b_a_5_a
        type: u4
        
      - id: iterator
        type: u4
      
      - id: bookmark_bits_1_2_8
        type: u8
      
      - id: storage_alloc_size
        type: u8
      
      - id: storage_used_size
        type: u8
        
      - id: segment_needs_resizing
        type: u1
        
      - id: compression_info
        type: u4
        
      - id: ss
        type: s_s_element
        
      - id: has_bit_packed_sub_seg
        type: u1
        
      - id: cs
        type: c_s1_element
      
      - id: cs_tag_end
        contents: ['CS:1>',0x00]

  s_s_element:
    seq:
      - id: ss_tag
        contents: ['<1:SS',0x00] 

      - id: distinct_states
        type: u8
      
      - id: min_data_id
        type: u4
        
      - id: max_data_id
        type: u4
      
      - id: original_min_segment_data_id
        type: u4

      - id: r_l_e_sort_order
        type: s8
        
      - id: row_count
        type: u8
      
      - id: has_nulls
        type: u1
        
      - id: r_l_e_runs
        type: u8
        
      - id: others_r_l_e_runs
        type: u8

      - id: ss_tag_end
        contents: ['SS:1>',0x00]

  c_s1_element:
    seq:
      - id: cs_tag
        contents: ['<1:CS',0x00] 
      
      - id: count_bit_packed
        type: u8
        
      - id: blob_with9_zeros
        size: 9
      
      - id: cs_tag_end
        contents: ['CS:1>',0x00]

  s_d_os_element:
    seq:
      - id: sdos_tag
        contents: ['<1:SDOs',0x00] 
      
      - id: csdos
        type: c_s_d_os_element
        
      - id: sdos_tag_end
        contents: ['SDOs:1>',0x00] 

  c_s_d_os_element:
    seq:
      - id: csdos_tag
        contents: ['<1:CSDOs',0x00]
      
      - id: zero_c_s_d_o
        type: u8
        
      - id: primary_segment_size
        type: u8
      
      - id: csdos
        type: c_s_d_os1_element

      - id: csdos_tag_end
        contents: ['CSDOs:1>',0x00]

  c_s_d_os1_element:
    seq:
      - id: csdos_tag
        contents: ['<1:CSDOs',0x00]
      
      - id: sub_segment_offset
        type: u8
      
      - id: sub_segment_size
        type: u8
  
      - id: csdos_tag_end
        contents: ['CSDOs:1>',0x00]
instances:
  bit_width:
    value: 36 - blocks.cp.cs.a_b_a_5_a + blocks.cp.cs.iterator

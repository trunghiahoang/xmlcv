"""
Basic usage example for XMLCV
"""

from pathlib import Path
from xmlcv import XMLToHTMLConverter, ConverterConfig

# Example 1: Basic conversion
def example_basic():
    """Basic file conversion"""
    converter = XMLToHTMLConverter()
    
    xml_file = Path("input.xml")
    html_file = Path("output.html")
    
    html = converter.convert_file(xml_file, html_file)
    print(f"✅ Converted {xml_file} to {html_file}")


# Example 2: With custom configuration
def example_custom_config():
    """Conversion with custom configuration"""
    config = ConverterConfig(
        convert_to_pdf=True,
        include_navigation=True,
        include_toc=True,
        create_index=True
    )
    
    converter = XMLToHTMLConverter(config)
    
    xml_file = Path("input.xml")
    html_file = Path("output.html")
    
    converter.convert_file(xml_file, html_file)


# Example 3: Custom element processor
def example_custom_processor():
    """Using custom element processor"""
    import xml.etree.ElementTree as ET
    
    def my_custom_processor(element: ET.Element, context: dict) -> str:
        """Custom processor for MyCustomElement"""
        text = element.text or ""
        return f'<div class="custom-element">{text}</div>'
    
    config = ConverterConfig()
    config.element_processors['MyCustomElement'] = my_custom_processor
    
    converter = XMLToHTMLConverter(config)
    converter.convert_file(Path("input.xml"), Path("output.html"))


# Example 4: Analyze XML structure
def example_analyze():
    """Analyze XML structure"""
    converter = XMLToHTMLConverter()
    
    structure = converter.analyze_xml(Path("input.xml"))
    
    print("XML Structure:")
    print(f"  Elements: {structure.get('elements', set())}")
    print(f"  Hierarchy: {structure.get('hierarchy', {})}")


# Example 5: Batch conversion
def example_batch():
    """Convert entire directory"""
    converter = XMLToHTMLConverter()
    
    input_dir = Path("xml_files/")
    output_dir = Path("html_output/")
    
    converted = converter.convert_directory(input_dir, output_dir)
    print(f"✅ Converted {len(converted)} files")


if __name__ == "__main__":
    print("XMLCV - Examples")
    print("See function definitions for usage examples")


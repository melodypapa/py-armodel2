"""DiagnosticDataElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 41)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 982)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArraySizeSemanticsEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class DiagnosticDataElement(Identifiable):
    """AUTOSAR DiagnosticDataElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-DATA-ELEMENT"


    array_size_semantics: Optional[ArraySizeSemanticsEnum]
    max_number_of_elements: Optional[PositiveInteger]
    scaling_info_size: Optional[PositiveInteger]
    sw_data_def_props: Optional[SwDataDefProps]
    _DESERIALIZE_DISPATCH = {
        "ARRAY-SIZE-SEMANTICS": lambda obj, elem: setattr(obj, "array_size_semantics", ArraySizeSemanticsEnum.deserialize(elem)),
        "MAX-NUMBER-OF-ELEMENTS": lambda obj, elem: setattr(obj, "max_number_of_elements", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SCALING-INFO-SIZE": lambda obj, elem: setattr(obj, "scaling_info_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SW-DATA-DEF-PROPS": lambda obj, elem: setattr(obj, "sw_data_def_props", SerializationHelper.deserialize_by_tag(elem, "SwDataDefProps")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticDataElement."""
        super().__init__()
        self.array_size_semantics: Optional[ArraySizeSemanticsEnum] = None
        self.max_number_of_elements: Optional[PositiveInteger] = None
        self.scaling_info_size: Optional[PositiveInteger] = None
        self.sw_data_def_props: Optional[SwDataDefProps] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDataElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDataElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize array_size_semantics
        if self.array_size_semantics is not None:
            serialized = SerializationHelper.serialize_item(self.array_size_semantics, "ArraySizeSemanticsEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-SIZE-SEMANTICS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_number_of_elements
        if self.max_number_of_elements is not None:
            serialized = SerializationHelper.serialize_item(self.max_number_of_elements, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF-ELEMENTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize scaling_info_size
        if self.scaling_info_size is not None:
            serialized = SerializationHelper.serialize_item(self.scaling_info_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCALING-INFO-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_data_def_props
        if self.sw_data_def_props is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_def_props, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEF-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataElement":
        """Deserialize XML element to DiagnosticDataElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDataElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDataElement, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ARRAY-SIZE-SEMANTICS":
                setattr(obj, "array_size_semantics", ArraySizeSemanticsEnum.deserialize(child))
            elif tag == "MAX-NUMBER-OF-ELEMENTS":
                setattr(obj, "max_number_of_elements", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SCALING-INFO-SIZE":
                setattr(obj, "scaling_info_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SW-DATA-DEF-PROPS":
                setattr(obj, "sw_data_def_props", SerializationHelper.deserialize_by_tag(child, "SwDataDefProps"))

        return obj



class DiagnosticDataElementBuilder(IdentifiableBuilder):
    """Builder for DiagnosticDataElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticDataElement = DiagnosticDataElement()


    def with_array_size_semantics(self, value: Optional[ArraySizeSemanticsEnum]) -> "DiagnosticDataElementBuilder":
        """Set array_size_semantics attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'array_size_semantics' is required and cannot be None")
        self._obj.array_size_semantics = value
        return self

    def with_max_number_of_elements(self, value: Optional[PositiveInteger]) -> "DiagnosticDataElementBuilder":
        """Set max_number_of_elements attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max_number_of_elements' is required and cannot be None")
        self._obj.max_number_of_elements = value
        return self

    def with_scaling_info_size(self, value: Optional[PositiveInteger]) -> "DiagnosticDataElementBuilder":
        """Set scaling_info_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'scaling_info_size' is required and cannot be None")
        self._obj.scaling_info_size = value
        return self

    def with_sw_data_def_props(self, value: Optional[SwDataDefProps]) -> "DiagnosticDataElementBuilder":
        """Set sw_data_def_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_data_def_props' is required and cannot be None")
        self._obj.sw_data_def_props = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "arraySizeSemantics",
        "maxNumberOfElements",
        "scalingInfoSize",
        "swDataDefProps",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticDataElement:
        """Build and return the DiagnosticDataElement instance with validation."""
        self._validate_instance()
        return self._obj
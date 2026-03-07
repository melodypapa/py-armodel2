"""SwPointerTargetProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 39)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 286)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 471)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
        BswModuleEntry,
    )
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SwPointerTargetProps(ARObject):
    """AUTOSAR SwPointerTargetProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-POINTER-TARGET-PROPS"


    target_category: Optional[Identifier]
    function_pointer_signature_ref: Optional[ARRef]
    sw_data_def_props: Optional[SwDataDefProps]
    _DESERIALIZE_DISPATCH = {
        "TARGET-CATEGORY": lambda obj, elem: setattr(obj, "target_category", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "FUNCTION-POINTER-SIGNATURE-REF": lambda obj, elem: setattr(obj, "function_pointer_signature_ref", ARRef.deserialize(elem)),
        "SW-DATA-DEF-PROPS": lambda obj, elem: setattr(obj, "sw_data_def_props", SerializationHelper.deserialize_by_tag(elem, "SwDataDefProps")),
    }


    def __init__(self) -> None:
        """Initialize SwPointerTargetProps."""
        super().__init__()
        self.target_category: Optional[Identifier] = None
        self.function_pointer_signature_ref: Optional[ARRef] = None
        self.sw_data_def_props: Optional[SwDataDefProps] = None

    def serialize(self) -> ET.Element:
        """Serialize SwPointerTargetProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwPointerTargetProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize target_category
        if self.target_category is not None:
            serialized = SerializationHelper.serialize_item(self.target_category, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize function_pointer_signature_ref
        if self.function_pointer_signature_ref is not None:
            serialized = SerializationHelper.serialize_item(self.function_pointer_signature_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION-POINTER-SIGNATURE-REF")
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
    def deserialize(cls, element: ET.Element) -> "SwPointerTargetProps":
        """Deserialize XML element to SwPointerTargetProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwPointerTargetProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwPointerTargetProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TARGET-CATEGORY":
                setattr(obj, "target_category", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "FUNCTION-POINTER-SIGNATURE-REF":
                setattr(obj, "function_pointer_signature_ref", ARRef.deserialize(child))
            elif tag == "SW-DATA-DEF-PROPS":
                setattr(obj, "sw_data_def_props", SerializationHelper.deserialize_by_tag(child, "SwDataDefProps"))

        return obj



class SwPointerTargetPropsBuilder(BuilderBase):
    """Builder for SwPointerTargetProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwPointerTargetProps = SwPointerTargetProps()


    def with_target_category(self, value: Optional[Identifier]) -> "SwPointerTargetPropsBuilder":
        """Set target_category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'target_category' is required and cannot be None")
        self._obj.target_category = value
        return self

    def with_function_pointer_signature(self, value: Optional[BswModuleEntry]) -> "SwPointerTargetPropsBuilder":
        """Set function_pointer_signature attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'function_pointer_signature' is required and cannot be None")
        self._obj.function_pointer_signature = value
        return self

    def with_sw_data_def_props(self, value: Optional[SwDataDefProps]) -> "SwPointerTargetPropsBuilder":
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
        "functionPointerSignature",
        "swDataDefProps",
        "targetCategory",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwPointerTargetProps:
        """Build and return the SwPointerTargetProps instance with validation."""
        self._validate_instance()
        return self._obj
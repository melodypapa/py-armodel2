"""SystemSignal AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 332)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1009)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 218)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SystemSignal(ARElement):
    """AUTOSAR SystemSignal."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SYSTEM-SIGNAL"


    dynamic_length: Optional[Boolean]
    physical_props: Optional[SwDataDefProps]
    _DESERIALIZE_DISPATCH = {
        "DYNAMIC-LENGTH": lambda obj, elem: setattr(obj, "dynamic_length", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "PHYSICAL-PROPS": lambda obj, elem: setattr(obj, "physical_props", SerializationHelper.deserialize_by_tag(elem, "SwDataDefProps")),
    }


    def __init__(self) -> None:
        """Initialize SystemSignal."""
        super().__init__()
        self.dynamic_length: Optional[Boolean] = None
        self.physical_props: Optional[SwDataDefProps] = None

    def serialize(self) -> ET.Element:
        """Serialize SystemSignal to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SystemSignal, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamic_length
        if self.dynamic_length is not None:
            serialized = SerializationHelper.serialize_item(self.dynamic_length, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize physical_props
        if self.physical_props is not None:
            serialized = SerializationHelper.serialize_item(self.physical_props, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemSignal":
        """Deserialize XML element to SystemSignal object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SystemSignal object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SystemSignal, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DYNAMIC-LENGTH":
                setattr(obj, "dynamic_length", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "PHYSICAL-PROPS":
                setattr(obj, "physical_props", SerializationHelper.deserialize_by_tag(child, "SwDataDefProps"))

        return obj



class SystemSignalBuilder(ARElementBuilder):
    """Builder for SystemSignal with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SystemSignal = SystemSignal()


    def with_dynamic_length(self, value: Optional[Boolean]) -> "SystemSignalBuilder":
        """Set dynamic_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dynamic_length = value
        return self

    def with_physical_props(self, value: Optional[SwDataDefProps]) -> "SystemSignalBuilder":
        """Set physical_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.physical_props = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dynamicLength",
        "physicalProps",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SystemSignal:
        """Build and return the SystemSignal instance with validation."""
        self._validate_instance()
        return self._obj
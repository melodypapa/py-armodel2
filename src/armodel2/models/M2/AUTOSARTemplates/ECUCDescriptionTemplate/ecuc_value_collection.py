"""EcucValueCollection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 108)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2022)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 222)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucValueCollection(ARElement):
    """AUTOSAR EcucValueCollection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-VALUE-COLLECTION"


    ecuc_value_refs: list[Any]
    ecu_extract_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ECUC-VALUE-REFS": lambda obj, elem: [obj.ecuc_value_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "ECU-EXTRACT-REF": lambda obj, elem: setattr(obj, "ecu_extract_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize EcucValueCollection."""
        super().__init__()
        self.ecuc_value_refs: list[Any] = []
        self.ecu_extract_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucValueCollection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucValueCollection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecuc_value_refs (list to container "ECUC-VALUE-REFS")
        if self.ecuc_value_refs:
            wrapper = ET.Element("ECUC-VALUE-REFS")
            for item in self.ecuc_value_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("ECUC-VALUE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_extract_ref
        if self.ecu_extract_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_extract_ref, "System")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-EXTRACT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucValueCollection":
        """Deserialize XML element to EcucValueCollection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucValueCollection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucValueCollection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ECUC-VALUE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.ecuc_value_refs.append(ARRef.deserialize(item_elem))
            elif tag == "ECU-EXTRACT-REF":
                setattr(obj, "ecu_extract_ref", ARRef.deserialize(child))

        return obj



class EcucValueCollectionBuilder(ARElementBuilder):
    """Builder for EcucValueCollection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucValueCollection = EcucValueCollection()


    def with_ecuc_values(self, items: list[Any]) -> "EcucValueCollectionBuilder":
        """Set ecuc_values list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecuc_values = list(items) if items else []
        return self

    def with_ecu_extract(self, value: Optional[System]) -> "EcucValueCollectionBuilder":
        """Set ecu_extract attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'ecu_extract' is required and cannot be None")
        self._obj.ecu_extract = value
        return self


    def add_ecuc_value(self, item: Any) -> "EcucValueCollectionBuilder":
        """Add a single item to ecuc_values list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecuc_values.append(item)
        return self

    def clear_ecuc_values(self) -> "EcucValueCollectionBuilder":
        """Clear all items from ecuc_values list.

        Returns:
            self for method chaining
        """
        self._obj.ecuc_values = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ecuExtract",
        "ecucValue",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucValueCollection:
        """Build and return the EcucValueCollection instance with validation."""
        self._validate_instance()
        return self._obj
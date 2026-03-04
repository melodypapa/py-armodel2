"""AclOperation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 384)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AclOperation(ARElement):
    """AUTOSAR AclOperation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ACL-OPERATION"


    implied_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "IMPLIED-REFS": lambda obj, elem: [obj.implied_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize AclOperation."""
        super().__init__()
        self.implied_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize AclOperation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AclOperation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize implied_refs (list to container "IMPLIED-REFS")
        if self.implied_refs:
            wrapper = ET.Element("IMPLIED-REFS")
            for item in self.implied_refs:
                serialized = SerializationHelper.serialize_item(item, "AclOperation")
                if serialized is not None:
                    child_elem = ET.Element("IMPLIED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclOperation":
        """Deserialize XML element to AclOperation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AclOperation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AclOperation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IMPLIED-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.implied_refs.append(ARRef.deserialize(item_elem))

        return obj



class AclOperationBuilder(ARElementBuilder):
    """Builder for AclOperation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AclOperation = AclOperation()


    def with_implieds(self, items: list[AclOperation]) -> "AclOperationBuilder":
        """Set implieds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.implieds = list(items) if items else []
        return self


    def add_implied(self, item: AclOperation) -> "AclOperationBuilder":
        """Add a single item to implieds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.implieds.append(item)
        return self

    def clear_implieds(self) -> "AclOperationBuilder":
        """Clear all items from implieds list.

        Returns:
            self for method chaining
        """
        self._obj.implieds = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "implied",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> AclOperation:
        """Build and return the AclOperation instance with validation."""
        self._validate_instance()
        return self._obj
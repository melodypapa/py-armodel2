"""EcucChoiceReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 74)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import (
    EcucAbstractInternalReferenceDef,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import EcucAbstractInternalReferenceDefBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucChoiceReferenceDef(EcucAbstractInternalReferenceDef):
    """AUTOSAR EcucChoiceReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-CHOICE-REFERENCE-DEF"


    destination_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DESTINATION-REFS": ("_POLYMORPHIC_LIST", "destination_refs", ["EcucChoiceContainerDef", "EcucParamConfContainerDef"]),
    }


    def __init__(self) -> None:
        """Initialize EcucChoiceReferenceDef."""
        super().__init__()
        self.destination_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucChoiceReferenceDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucChoiceReferenceDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_refs (list to container "DESTINATION-REFS")
        if self.destination_refs:
            wrapper = ET.Element("DESTINATION-REFS")
            for item in self.destination_refs:
                serialized = SerializationHelper.serialize_item(item, "EcucContainerDef")
                if serialized is not None:
                    child_elem = ET.Element("DESTINATION-REF")
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
    def deserialize(cls, element: ET.Element) -> "EcucChoiceReferenceDef":
        """Deserialize XML element to EcucChoiceReferenceDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucChoiceReferenceDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucChoiceReferenceDef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DESTINATION-REFS":
                for item_elem in child:
                    obj.destination_refs.append(ARRef.deserialize(item_elem))

        return obj



class EcucChoiceReferenceDefBuilder(EcucAbstractInternalReferenceDefBuilder):
    """Builder for EcucChoiceReferenceDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucChoiceReferenceDef = EcucChoiceReferenceDef()


    def with_destinations(self, items: list[EcucContainerDef]) -> "EcucChoiceReferenceDefBuilder":
        """Set destinations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.destinations = list(items) if items else []
        return self


    def add_destination(self, item: EcucContainerDef) -> "EcucChoiceReferenceDefBuilder":
        """Add a single item to destinations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.destinations.append(item)
        return self

    def clear_destinations(self) -> "EcucChoiceReferenceDefBuilder":
        """Clear all items from destinations list.

        Returns:
            self for method chaining
        """
        self._obj.destinations = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "destination",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucChoiceReferenceDef:
        """Build and return the EcucChoiceReferenceDef instance with validation."""
        self._validate_instance()
        return self._obj
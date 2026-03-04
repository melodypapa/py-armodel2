"""GeneralPurposeConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 388)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GeneralPurposeConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class GeneralPurposeConnection(ARElement):
    """AUTOSAR GeneralPurposeConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "GENERAL-PURPOSE-CONNECTION"


    pdu_triggering_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PDU-TRIGGERING-REFS": lambda obj, elem: [obj.pdu_triggering_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize GeneralPurposeConnection."""
        super().__init__()
        self.pdu_triggering_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize GeneralPurposeConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GeneralPurposeConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize pdu_triggering_refs (list to container "PDU-TRIGGERING-REFS")
        if self.pdu_triggering_refs:
            wrapper = ET.Element("PDU-TRIGGERING-REFS")
            for item in self.pdu_triggering_refs:
                serialized = SerializationHelper.serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("PDU-TRIGGERING-REF")
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
    def deserialize(cls, element: ET.Element) -> "GeneralPurposeConnection":
        """Deserialize XML element to GeneralPurposeConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GeneralPurposeConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GeneralPurposeConnection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PDU-TRIGGERING-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.pdu_triggering_refs.append(ARRef.deserialize(item_elem))

        return obj



class GeneralPurposeConnectionBuilder(ARElementBuilder):
    """Builder for GeneralPurposeConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: GeneralPurposeConnection = GeneralPurposeConnection()


    def with_pdu_triggerings(self, items: list[PduTriggering]) -> "GeneralPurposeConnectionBuilder":
        """Set pdu_triggerings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pdu_triggerings = list(items) if items else []
        return self


    def add_pdu_triggering(self, item: PduTriggering) -> "GeneralPurposeConnectionBuilder":
        """Add a single item to pdu_triggerings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pdu_triggerings.append(item)
        return self

    def clear_pdu_triggerings(self) -> "GeneralPurposeConnectionBuilder":
        """Clear all items from pdu_triggerings list.

        Returns:
            self for method chaining
        """
        self._obj.pdu_triggerings = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "pduTriggering",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> GeneralPurposeConnection:
        """Build and return the GeneralPurposeConnection instance with validation."""
        self._validate_instance()
        return self._obj
"""PdurIPduGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 352)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PdurIPduGroup(FibexElement):
    """AUTOSAR PdurIPduGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PDUR-I-PDU-GROUP"


    communication: Optional[String]
    i_pdu_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COMMUNICATION": lambda obj, elem: setattr(obj, "communication", SerializationHelper.deserialize_by_tag(elem, "String")),
        "I-PDU-REFS": lambda obj, elem: [obj.i_pdu_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize PdurIPduGroup."""
        super().__init__()
        self.communication: Optional[String] = None
        self.i_pdu_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PdurIPduGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PdurIPduGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication
        if self.communication is not None:
            serialized = SerializationHelper.serialize_item(self.communication, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_pdu_refs (list to container "I-PDU-REFS")
        if self.i_pdu_refs:
            wrapper = ET.Element("I-PDU-REFS")
            for item in self.i_pdu_refs:
                serialized = SerializationHelper.serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("I-PDU-REF")
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
    def deserialize(cls, element: ET.Element) -> "PdurIPduGroup":
        """Deserialize XML element to PdurIPduGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PdurIPduGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PdurIPduGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMMUNICATION":
                setattr(obj, "communication", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "I-PDU-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.i_pdu_refs.append(ARRef.deserialize(item_elem))

        return obj



class PdurIPduGroupBuilder(FibexElementBuilder):
    """Builder for PdurIPduGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PdurIPduGroup = PdurIPduGroup()


    def with_communication(self, value: Optional[String]) -> "PdurIPduGroupBuilder":
        """Set communication attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'communication' is required and cannot be None")
        self._obj.communication = value
        return self

    def with_i_pdus(self, items: list[PduTriggering]) -> "PdurIPduGroupBuilder":
        """Set i_pdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_pdus = list(items) if items else []
        return self


    def add_i_pdu(self, item: PduTriggering) -> "PdurIPduGroupBuilder":
        """Add a single item to i_pdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_pdus.append(item)
        return self

    def clear_i_pdus(self) -> "PdurIPduGroupBuilder":
        """Clear all items from i_pdus list.

        Returns:
            self for method chaining
        """
        self._obj.i_pdus = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "communication",
        "iPdu",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PdurIPduGroup:
        """Build and return the PdurIPduGroup instance with validation."""
        self._validate_instance()
        return self._obj
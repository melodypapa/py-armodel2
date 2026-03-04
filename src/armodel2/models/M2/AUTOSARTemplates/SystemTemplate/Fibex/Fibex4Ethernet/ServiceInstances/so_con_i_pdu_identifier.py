"""SoConIPduIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 489)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import ReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionTriggerEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SoConIPduIdentifier(Referrable):
    """AUTOSAR SoConIPduIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SO-CON-I-PDU-IDENTIFIER"


    header_id: Optional[PositiveInteger]
    pdu_collection_ref: Optional[Any]
    pdu_collection_trigger_ref: Optional[PduCollectionTriggerEnum]
    pdu_triggering_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "HEADER-ID": lambda obj, elem: setattr(obj, "header_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PDU-COLLECTION-REF": lambda obj, elem: setattr(obj, "pdu_collection_ref", ARRef.deserialize(elem)),
        "PDU-COLLECTION-TRIGGER-REF": lambda obj, elem: setattr(obj, "pdu_collection_trigger_ref", PduCollectionTriggerEnum.deserialize(elem)),
        "PDU-TRIGGERING-REF": lambda obj, elem: setattr(obj, "pdu_triggering_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SoConIPduIdentifier."""
        super().__init__()
        self.header_id: Optional[PositiveInteger] = None
        self.pdu_collection_ref: Optional[Any] = None
        self.pdu_collection_trigger_ref: Optional[PduCollectionTriggerEnum] = None
        self.pdu_triggering_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SoConIPduIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SoConIPduIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize header_id
        if self.header_id is not None:
            serialized = SerializationHelper.serialize_item(self.header_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEADER-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_collection_ref
        if self.pdu_collection_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_collection_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-COLLECTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_collection_trigger_ref
        if self.pdu_collection_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_collection_trigger_ref, "PduCollectionTriggerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-COLLECTION-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_triggering_ref
        if self.pdu_triggering_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_triggering_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-TRIGGERING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SoConIPduIdentifier":
        """Deserialize XML element to SoConIPduIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SoConIPduIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SoConIPduIdentifier, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "HEADER-ID":
                setattr(obj, "header_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PDU-COLLECTION-REF":
                setattr(obj, "pdu_collection_ref", ARRef.deserialize(child))
            elif tag == "PDU-COLLECTION-TRIGGER-REF":
                setattr(obj, "pdu_collection_trigger_ref", PduCollectionTriggerEnum.deserialize(child))
            elif tag == "PDU-TRIGGERING-REF":
                setattr(obj, "pdu_triggering_ref", ARRef.deserialize(child))

        return obj



class SoConIPduIdentifierBuilder(ReferrableBuilder):
    """Builder for SoConIPduIdentifier with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SoConIPduIdentifier = SoConIPduIdentifier()


    def with_header_id(self, value: Optional[PositiveInteger]) -> "SoConIPduIdentifierBuilder":
        """Set header_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.header_id = value
        return self

    def with_pdu_collection(self, value: Optional[any (PduCollection)]) -> "SoConIPduIdentifierBuilder":
        """Set pdu_collection attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdu_collection = value
        return self

    def with_pdu_collection_trigger(self, value: Optional[PduCollectionTriggerEnum]) -> "SoConIPduIdentifierBuilder":
        """Set pdu_collection_trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdu_collection_trigger = value
        return self

    def with_pdu_triggering(self, value: Optional[PduTriggering]) -> "SoConIPduIdentifierBuilder":
        """Set pdu_triggering attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdu_triggering = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "headerId",
        "pduCollection",
        "pduCollectionTrigger",
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


    def build(self) -> SoConIPduIdentifier:
        """Build and return the SoConIPduIdentifier instance with validation."""
        self._validate_instance()
        return self._obj
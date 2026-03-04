"""IEEE1722TpAcfBusPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 657)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionTriggerEnum,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IEEE1722TpAcfBusPart(Identifiable, ABC):
    """AUTOSAR IEEE1722TpAcfBusPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    collection_trigger_ref: Optional[PduCollectionTriggerEnum]
    _DESERIALIZE_DISPATCH = {
        "COLLECTION-TRIGGER-REF": lambda obj, elem: setattr(obj, "collection_trigger_ref", PduCollectionTriggerEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfBusPart."""
        super().__init__()
        self.collection_trigger_ref: Optional[PduCollectionTriggerEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfBusPart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfBusPart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize collection_trigger_ref
        if self.collection_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.collection_trigger_ref, "PduCollectionTriggerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLECTION-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfBusPart":
        """Deserialize XML element to IEEE1722TpAcfBusPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfBusPart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfBusPart, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COLLECTION-TRIGGER-REF":
                setattr(obj, "collection_trigger_ref", PduCollectionTriggerEnum.deserialize(child))

        return obj



class IEEE1722TpAcfBusPartBuilder(IdentifiableBuilder):
    """Builder for IEEE1722TpAcfBusPart with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpAcfBusPart = IEEE1722TpAcfBusPart()


    def with_collection_trigger(self, value: Optional[PduCollectionTriggerEnum]) -> "IEEE1722TpAcfBusPartBuilder":
        """Set collection_trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.collection_trigger = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "collectionTrigger",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> IEEE1722TpAcfBusPart:
        """Build and return the IEEE1722TpAcfBusPart instance (abstract)."""
        raise NotImplementedError
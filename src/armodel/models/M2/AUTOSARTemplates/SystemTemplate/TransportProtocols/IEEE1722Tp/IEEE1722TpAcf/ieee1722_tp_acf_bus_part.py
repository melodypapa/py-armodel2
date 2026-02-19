"""IEEE1722TpAcfBusPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 657)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionTriggerEnum,
)
from abc import ABC, abstractmethod


class IEEE1722TpAcfBusPart(Identifiable, ABC):
    """AUTOSAR IEEE1722TpAcfBusPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    collection_trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfBusPart."""
        super().__init__()
        self.collection_trigger_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfBusPart":
        """Deserialize XML element to IEEE1722TpAcfBusPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfBusPart object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse collection_trigger_ref
        child = ARObject._find_child_element(element, "COLLECTION-TRIGGER")
        if child is not None:
            collection_trigger_ref_value = child.text
            obj.collection_trigger_ref = collection_trigger_ref_value

        return obj



class IEEE1722TpAcfBusPartBuilder:
    """Builder for IEEE1722TpAcfBusPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfBusPart = IEEE1722TpAcfBusPart()

    def build(self) -> IEEE1722TpAcfBusPart:
        """Build and return IEEE1722TpAcfBusPart object.

        Returns:
            IEEE1722TpAcfBusPart instance
        """
        # TODO: Add validation
        return self._obj

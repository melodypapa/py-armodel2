"""EthTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 618)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class EthTpConnection(TpConnection):
    """AUTOSAR EthTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_sdu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize EthTpConnection."""
        super().__init__()
        self.tp_sdu_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize EthTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tp_sdu_refs (list to container "TP-SDUS")
        if self.tp_sdu_refs:
            wrapper = ET.Element("TP-SDUS")
            for item in self.tp_sdu_refs:
                serialized = ARObject._serialize_item(item, "PduTriggering")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTpConnection":
        """Deserialize XML element to EthTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthTpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthTpConnection, cls).deserialize(element)

        # Parse tp_sdu_refs (list from container "TP-SDUS")
        obj.tp_sdu_refs = []
        container = ARObject._find_child_element(element, "TP-SDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_sdu_refs.append(child_value)

        return obj



class EthTpConnectionBuilder:
    """Builder for EthTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTpConnection = EthTpConnection()

    def build(self) -> EthTpConnection:
        """Build and return EthTpConnection object.

        Returns:
            EthTpConnection instance
        """
        # TODO: Add validation
        return self._obj

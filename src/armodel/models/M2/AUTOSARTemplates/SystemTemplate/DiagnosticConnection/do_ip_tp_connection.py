"""DoIpTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 555)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DiagnosticConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class DoIpTpConnection(TpConnection):
    """AUTOSAR DoIpTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    do_ip_source_ref: Optional[ARRef]
    do_ip_target_ref: Optional[ARRef]
    tp_sdu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DoIpTpConnection."""
        super().__init__()
        self.do_ip_source_ref: Optional[ARRef] = None
        self.do_ip_target_ref: Optional[ARRef] = None
        self.tp_sdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DoIpTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize do_ip_source_ref
        if self.do_ip_source_ref is not None:
            serialized = ARObject._serialize_item(self.do_ip_source_ref, "DoIpLogicAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DO-IP-SOURCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize do_ip_target_ref
        if self.do_ip_target_ref is not None:
            serialized = ARObject._serialize_item(self.do_ip_target_ref, "DoIpLogicAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DO-IP-TARGET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_sdu_ref
        if self.tp_sdu_ref is not None:
            serialized = ARObject._serialize_item(self.tp_sdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpTpConnection":
        """Deserialize XML element to DoIpTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpTpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpTpConnection, cls).deserialize(element)

        # Parse do_ip_source_ref
        child = ARObject._find_child_element(element, "DO-IP-SOURCE-REF")
        if child is not None:
            do_ip_source_ref_value = ARRef.deserialize(child)
            obj.do_ip_source_ref = do_ip_source_ref_value

        # Parse do_ip_target_ref
        child = ARObject._find_child_element(element, "DO-IP-TARGET-REF")
        if child is not None:
            do_ip_target_ref_value = ARRef.deserialize(child)
            obj.do_ip_target_ref = do_ip_target_ref_value

        # Parse tp_sdu_ref
        child = ARObject._find_child_element(element, "TP-SDU-REF")
        if child is not None:
            tp_sdu_ref_value = ARRef.deserialize(child)
            obj.tp_sdu_ref = tp_sdu_ref_value

        return obj



class DoIpTpConnectionBuilder:
    """Builder for DoIpTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpTpConnection = DoIpTpConnection()

    def build(self) -> DoIpTpConnection:
        """Build and return DoIpTpConnection object.

        Returns:
            DoIpTpConnection instance
        """
        # TODO: Add validation
        return self._obj

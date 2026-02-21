"""J1939TpPg AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 625)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class J1939TpPg(ARObject):
    """AUTOSAR J1939TpPg."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    direct_pdu_ref: Optional[ARRef]
    pgn: Optional[Integer]
    requestable: Optional[Boolean]
    sdu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize J1939TpPg."""
        super().__init__()
        self.direct_pdu_ref: Optional[ARRef] = None
        self.pgn: Optional[Integer] = None
        self.requestable: Optional[Boolean] = None
        self.sdu_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize J1939TpPg to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize direct_pdu_ref
        if self.direct_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.direct_pdu_ref, "NPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECT-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pgn
        if self.pgn is not None:
            serialized = SerializationHelper.serialize_item(self.pgn, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PGN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize requestable
        if self.requestable is not None:
            serialized = SerializationHelper.serialize_item(self.requestable, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUESTABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdu_refs (list to container "SDU-REFS")
        if self.sdu_refs:
            wrapper = ET.Element("SDU-REFS")
            for item in self.sdu_refs:
                serialized = SerializationHelper.serialize_item(item, "IPdu")
                if serialized is not None:
                    child_elem = ET.Element("SDU-REF")
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
    def deserialize(cls, element: ET.Element) -> "J1939TpPg":
        """Deserialize XML element to J1939TpPg object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939TpPg object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse direct_pdu_ref
        child = SerializationHelper.find_child_element(element, "DIRECT-PDU-REF")
        if child is not None:
            direct_pdu_ref_value = ARRef.deserialize(child)
            obj.direct_pdu_ref = direct_pdu_ref_value

        # Parse pgn
        child = SerializationHelper.find_child_element(element, "PGN")
        if child is not None:
            pgn_value = child.text
            obj.pgn = pgn_value

        # Parse requestable
        child = SerializationHelper.find_child_element(element, "REQUESTABLE")
        if child is not None:
            requestable_value = child.text
            obj.requestable = requestable_value

        # Parse sdu_refs (list from container "SDU-REFS")
        obj.sdu_refs = []
        container = SerializationHelper.find_child_element(element, "SDU-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdu_refs.append(child_value)

        return obj



class J1939TpPgBuilder:
    """Builder for J1939TpPg."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939TpPg = J1939TpPg()

    def build(self) -> J1939TpPg:
        """Build and return J1939TpPg object.

        Returns:
            J1939TpPg instance
        """
        # TODO: Add validation
        return self._obj

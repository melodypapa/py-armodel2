"""TpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 633)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DiagnosticConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection_ident import (
    TpConnectionIdent,
)
from abc import ABC, abstractmethod


class TpConnection(ARObject, ABC):
    """AUTOSAR TpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    ident: Optional[TpConnectionIdent]
    def __init__(self) -> None:
        """Initialize TpConnection."""
        super().__init__()
        self.ident: Optional[TpConnectionIdent] = None

    def serialize(self) -> ET.Element:
        """Serialize TpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ident
        if self.ident is not None:
            serialized = SerializationHelper.serialize_item(self.ident, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TpConnection":
        """Deserialize XML element to TpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TpConnection, cls).deserialize(element)

        # Parse ident
        child = SerializationHelper.find_child_element(element, "IDENT")
        if child is not None:
            ident_value = SerializationHelper.deserialize_by_tag(child, "TpConnectionIdent")
            obj.ident = ident_value

        return obj



class TpConnectionBuilder:
    """Builder for TpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpConnection = TpConnection()

    def build(self) -> TpConnection:
        """Build and return TpConnection object.

        Returns:
            TpConnection instance
        """
        # TODO: Add validation
        return self._obj

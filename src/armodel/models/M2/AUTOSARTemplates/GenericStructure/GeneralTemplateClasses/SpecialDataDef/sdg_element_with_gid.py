"""SdgElementWithGid AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from abc import ABC, abstractmethod


class SdgElementWithGid(ARObject, ABC):
    """AUTOSAR SdgElementWithGid."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    gid: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize SdgElementWithGid."""
        super().__init__()
        self.gid: Optional[NameToken] = None
    def serialize(self) -> ET.Element:
        """Serialize SdgElementWithGid to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize gid
        if self.gid is not None:
            serialized = ARObject._serialize_item(self.gid, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgElementWithGid":
        """Deserialize XML element to SdgElementWithGid object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgElementWithGid object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse gid
        child = ARObject._find_child_element(element, "GID")
        if child is not None:
            gid_value = child.text
            obj.gid = gid_value

        return obj



class SdgElementWithGidBuilder:
    """Builder for SdgElementWithGid."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgElementWithGid = SdgElementWithGid()

    def build(self) -> SdgElementWithGid:
        """Build and return SdgElementWithGid object.

        Returns:
            SdgElementWithGid instance
        """
        # TODO: Add validation
        return self._obj

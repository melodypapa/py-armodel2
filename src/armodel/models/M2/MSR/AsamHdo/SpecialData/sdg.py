"""Sdg AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1004)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 78)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 90)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg_caption import (
    SdgCaption,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg_contents import (
        SdgContents,
    )



class Sdg(ARObject):
    """AUTOSAR Sdg."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    gid: NameToken
    sdg_caption: Optional[SdgCaption]
    sdg_contents: Optional[SdgContents]
    def __init__(self) -> None:
        """Initialize Sdg."""
        super().__init__()
        self.gid: NameToken = None
        self.sdg_caption: Optional[SdgCaption] = None
        self.sdg_contents: Optional[SdgContents] = None

    def serialize(self) -> ET.Element:
        """Serialize Sdg to XML element.

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

        # Serialize sdg_caption
        if self.sdg_caption is not None:
            serialized = ARObject._serialize_item(self.sdg_caption, "SdgCaption")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDG-CAPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdg_contents
        if self.sdg_contents is not None:
            serialized = ARObject._serialize_item(self.sdg_contents, "SdgContents")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDG-CONTENTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Sdg":
        """Deserialize XML element to Sdg object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Sdg object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse gid
        child = ARObject._find_child_element(element, "GID")
        if child is not None:
            gid_value = child.text
            obj.gid = gid_value

        # Parse sdg_caption
        child = ARObject._find_child_element(element, "SDG-CAPTION")
        if child is not None:
            sdg_caption_value = ARObject._deserialize_by_tag(child, "SdgCaption")
            obj.sdg_caption = sdg_caption_value

        # Parse sdg_contents
        child = ARObject._find_child_element(element, "SDG-CONTENTS")
        if child is not None:
            sdg_contents_value = ARObject._deserialize_by_tag(child, "SdgContents")
            obj.sdg_contents = sdg_contents_value

        return obj



class SdgBuilder:
    """Builder for Sdg."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Sdg = Sdg()

    def build(self) -> Sdg:
        """Build and return Sdg object.

        Returns:
            Sdg instance
        """
        # TODO: Add validation
        return self._obj

"""MixedContentForPlainText AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 349)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class MixedContentForPlainText(ARObject, ABC):
    """AUTOSAR MixedContentForPlainText."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize MixedContentForPlainText."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize MixedContentForPlainText to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MixedContentForPlainText":
        """Deserialize XML element to MixedContentForPlainText object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MixedContentForPlainText object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class MixedContentForPlainTextBuilder:
    """Builder for MixedContentForPlainText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForPlainText = MixedContentForPlainText()

    def build(self) -> MixedContentForPlainText:
        """Build and return MixedContentForPlainText object.

        Returns:
            MixedContentForPlainText instance
        """
        # TODO: Add validation
        return self._obj

"""MixedContentForUnitNames AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 456)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)
from abc import ABC, abstractmethod


class MixedContentForUnitNames(ARObject, ABC):
    """AUTOSAR MixedContentForUnitNames."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    sub: Superscript
    sup: Superscript
    def __init__(self) -> None:
        """Initialize MixedContentForUnitNames."""
        super().__init__()
        self.sub: Superscript = None
        self.sup: Superscript = None
    def serialize(self) -> ET.Element:
        """Serialize MixedContentForUnitNames to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize sub
        if self.sub is not None:
            serialized = ARObject._serialize_item(self.sub, "Superscript")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUB")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sup
        if self.sup is not None:
            serialized = ARObject._serialize_item(self.sup, "Superscript")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MixedContentForUnitNames":
        """Deserialize XML element to MixedContentForUnitNames object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MixedContentForUnitNames object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sub
        child = ARObject._find_child_element(element, "SUB")
        if child is not None:
            sub_value = child.text
            obj.sub = sub_value

        # Parse sup
        child = ARObject._find_child_element(element, "SUP")
        if child is not None:
            sup_value = child.text
            obj.sup = sup_value

        return obj



class MixedContentForUnitNamesBuilder:
    """Builder for MixedContentForUnitNames."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForUnitNames = MixedContentForUnitNames()

    def build(self) -> MixedContentForUnitNames:
        """Build and return MixedContentForUnitNames object.

        Returns:
            MixedContentForUnitNames instance
        """
        # TODO: Add validation
        return self._obj

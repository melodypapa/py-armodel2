"""EmphasisText AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 316)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import (
    EEnum,
    EEnumFont,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)


class EmphasisText(ARObject):
    """AUTOSAR EmphasisText."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    color: Optional[String]
    font: Optional[EEnumFont]
    sub: Superscript
    sup: Superscript
    tt: Optional[Tt]
    type: Optional[EEnum]
    def __init__(self) -> None:
        """Initialize EmphasisText."""
        super().__init__()
        self.color: Optional[String] = None
        self.font: Optional[EEnumFont] = None
        self.sub: Superscript = None
        self.sup: Superscript = None
        self.tt: Optional[Tt] = None
        self.type: Optional[EEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize EmphasisText to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize color
        if self.color is not None:
            serialized = ARObject._serialize_item(self.color, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize font
        if self.font is not None:
            serialized = ARObject._serialize_item(self.font, "EEnumFont")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FONT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize tt
        if self.tt is not None:
            serialized = ARObject._serialize_item(self.tt, "Tt")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type
        if self.type is not None:
            serialized = ARObject._serialize_item(self.type, "EEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EmphasisText":
        """Deserialize XML element to EmphasisText object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EmphasisText object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse color
        child = ARObject._find_child_element(element, "COLOR")
        if child is not None:
            color_value = child.text
            obj.color = color_value

        # Parse font
        child = ARObject._find_child_element(element, "FONT")
        if child is not None:
            font_value = EEnumFont.deserialize(child)
            obj.font = font_value

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

        # Parse tt
        child = ARObject._find_child_element(element, "TT")
        if child is not None:
            tt_value = ARObject._deserialize_by_tag(child, "Tt")
            obj.tt = tt_value

        # Parse type
        child = ARObject._find_child_element(element, "TYPE")
        if child is not None:
            type_value = EEnum.deserialize(child)
            obj.type = type_value

        return obj



class EmphasisTextBuilder:
    """Builder for EmphasisText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EmphasisText = EmphasisText()

    def build(self) -> EmphasisText:
        """Build and return EmphasisText object.

        Returns:
            EmphasisText instance
        """
        # TODO: Add validation
        return self._obj

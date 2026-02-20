"""Entry AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 336)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    AlignEnum,
    ValignEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    TableSeparatorString,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class Entry(ARObject):
    """AUTOSAR Entry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    align: Optional[AlignEnum]
    bgcolor: String
    colname: Optional[String]
    colsep: Optional[TableSeparatorString]
    entry_contents: DocumentationBlock
    morerows: Optional[String]
    nameend: Optional[String]
    namest: Optional[String]
    rotate: Optional[String]
    rowsep: Optional[TableSeparatorString]
    spanname: Optional[String]
    valign: Optional[ValignEnum]
    def __init__(self) -> None:
        """Initialize Entry."""
        super().__init__()
        self.align: Optional[AlignEnum] = None
        self.bgcolor: String = None
        self.colname: Optional[String] = None
        self.colsep: Optional[TableSeparatorString] = None
        self.entry_contents: DocumentationBlock = None
        self.morerows: Optional[String] = None
        self.nameend: Optional[String] = None
        self.namest: Optional[String] = None
        self.rotate: Optional[String] = None
        self.rowsep: Optional[TableSeparatorString] = None
        self.spanname: Optional[String] = None
        self.valign: Optional[ValignEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize Entry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize align
        if self.align is not None:
            serialized = ARObject._serialize_item(self.align, "AlignEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIGN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize bgcolor
        if self.bgcolor is not None:
            serialized = ARObject._serialize_item(self.bgcolor, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BGCOLOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize colname
        if self.colname is not None:
            serialized = ARObject._serialize_item(self.colname, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLNAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize colsep
        if self.colsep is not None:
            serialized = ARObject._serialize_item(self.colsep, "TableSeparatorString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLSEP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize entry_contents
        if self.entry_contents is not None:
            serialized = ARObject._serialize_item(self.entry_contents, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENTRY-CONTENTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize morerows
        if self.morerows is not None:
            serialized = ARObject._serialize_item(self.morerows, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MOREROWS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nameend
        if self.nameend is not None:
            serialized = ARObject._serialize_item(self.nameend, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NAMEEND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize namest
        if self.namest is not None:
            serialized = ARObject._serialize_item(self.namest, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NAMEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rotate
        if self.rotate is not None:
            serialized = ARObject._serialize_item(self.rotate, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROTATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rowsep
        if self.rowsep is not None:
            serialized = ARObject._serialize_item(self.rowsep, "TableSeparatorString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROWSEP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize spanname
        if self.spanname is not None:
            serialized = ARObject._serialize_item(self.spanname, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPANNAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize valign
        if self.valign is not None:
            serialized = ARObject._serialize_item(self.valign, "ValignEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALIGN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Entry":
        """Deserialize XML element to Entry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Entry object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse align
        child = ARObject._find_child_element(element, "ALIGN")
        if child is not None:
            align_value = AlignEnum.deserialize(child)
            obj.align = align_value

        # Parse bgcolor
        child = ARObject._find_child_element(element, "BGCOLOR")
        if child is not None:
            bgcolor_value = child.text
            obj.bgcolor = bgcolor_value

        # Parse colname
        child = ARObject._find_child_element(element, "COLNAME")
        if child is not None:
            colname_value = child.text
            obj.colname = colname_value

        # Parse colsep
        child = ARObject._find_child_element(element, "COLSEP")
        if child is not None:
            colsep_value = child.text
            obj.colsep = colsep_value

        # Parse entry_contents
        child = ARObject._find_child_element(element, "ENTRY-CONTENTS")
        if child is not None:
            entry_contents_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.entry_contents = entry_contents_value

        # Parse morerows
        child = ARObject._find_child_element(element, "MOREROWS")
        if child is not None:
            morerows_value = child.text
            obj.morerows = morerows_value

        # Parse nameend
        child = ARObject._find_child_element(element, "NAMEEND")
        if child is not None:
            nameend_value = child.text
            obj.nameend = nameend_value

        # Parse namest
        child = ARObject._find_child_element(element, "NAMEST")
        if child is not None:
            namest_value = child.text
            obj.namest = namest_value

        # Parse rotate
        child = ARObject._find_child_element(element, "ROTATE")
        if child is not None:
            rotate_value = child.text
            obj.rotate = rotate_value

        # Parse rowsep
        child = ARObject._find_child_element(element, "ROWSEP")
        if child is not None:
            rowsep_value = child.text
            obj.rowsep = rowsep_value

        # Parse spanname
        child = ARObject._find_child_element(element, "SPANNAME")
        if child is not None:
            spanname_value = child.text
            obj.spanname = spanname_value

        # Parse valign
        child = ARObject._find_child_element(element, "VALIGN")
        if child is not None:
            valign_value = ValignEnum.deserialize(child)
            obj.valign = valign_value

        return obj



class EntryBuilder:
    """Builder for Entry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Entry = Entry()

    def build(self) -> Entry:
        """Build and return Entry object.

        Returns:
            Entry instance
        """
        # TODO: Add validation
        return self._obj

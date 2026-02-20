"""MsrQueryProps AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_arg import (
    MsrQueryArg,
)


class MsrQueryProps(ARObject):
    """AUTOSAR MsrQueryProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    comment: Optional[String]
    msr_query_args: list[MsrQueryArg]
    msr_query_name: String
    def __init__(self) -> None:
        """Initialize MsrQueryProps."""
        super().__init__()
        self.comment: Optional[String] = None
        self.msr_query_args: list[MsrQueryArg] = []
        self.msr_query_name: String = None

    def serialize(self) -> ET.Element:
        """Serialize MsrQueryProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize comment
        if self.comment is not None:
            serialized = ARObject._serialize_item(self.comment, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize msr_query_args (list to container "MSR-QUERY-ARGS")
        if self.msr_query_args:
            wrapper = ET.Element("MSR-QUERY-ARGS")
            for item in self.msr_query_args:
                serialized = ARObject._serialize_item(item, "MsrQueryArg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize msr_query_name
        if self.msr_query_name is not None:
            serialized = ARObject._serialize_item(self.msr_query_name, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryProps":
        """Deserialize XML element to MsrQueryProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse comment
        child = ARObject._find_child_element(element, "COMMENT")
        if child is not None:
            comment_value = child.text
            obj.comment = comment_value

        # Parse msr_query_args (list from container "MSR-QUERY-ARGS")
        obj.msr_query_args = []
        container = ARObject._find_child_element(element, "MSR-QUERY-ARGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.msr_query_args.append(child_value)

        # Parse msr_query_name
        child = ARObject._find_child_element(element, "MSR-QUERY-NAME")
        if child is not None:
            msr_query_name_value = child.text
            obj.msr_query_name = msr_query_name_value

        return obj



class MsrQueryPropsBuilder:
    """Builder for MsrQueryProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryProps = MsrQueryProps()

    def build(self) -> MsrQueryProps:
        """Build and return MsrQueryProps object.

        Returns:
            MsrQueryProps instance
        """
        # TODO: Add validation
        return self._obj

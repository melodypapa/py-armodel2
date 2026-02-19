"""DltArgument AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 983)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 13)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class DltArgument(Identifiable):
    """AUTOSAR DltArgument."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dlt_arguments: list[DltArgument]
    length: Optional[PositiveInteger]
    network: Optional[SwDataDefProps]
    optional: Optional[Boolean]
    predefined_text: Optional[Boolean]
    variable_length: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DltArgument."""
        super().__init__()
        self.dlt_arguments: list[DltArgument] = []
        self.length: Optional[PositiveInteger] = None
        self.network: Optional[SwDataDefProps] = None
        self.optional: Optional[Boolean] = None
        self.predefined_text: Optional[Boolean] = None
        self.variable_length: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize DltArgument to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltArgument, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dlt_arguments (list to container "DLT-ARGUMENTS")
        if self.dlt_arguments:
            wrapper = ET.Element("DLT-ARGUMENTS")
            for item in self.dlt_arguments:
                serialized = ARObject._serialize_item(item, "DltArgument")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize length
        if self.length is not None:
            serialized = ARObject._serialize_item(self.length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network
        if self.network is not None:
            serialized = ARObject._serialize_item(self.network, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize optional
        if self.optional is not None:
            serialized = ARObject._serialize_item(self.optional, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPTIONAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize predefined_text
        if self.predefined_text is not None:
            serialized = ARObject._serialize_item(self.predefined_text, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PREDEFINED-TEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variable_length
        if self.variable_length is not None:
            serialized = ARObject._serialize_item(self.variable_length, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltArgument":
        """Deserialize XML element to DltArgument object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltArgument object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltArgument, cls).deserialize(element)

        # Parse dlt_arguments (list from container "DLT-ARGUMENTS")
        obj.dlt_arguments = []
        container = ARObject._find_child_element(element, "DLT-ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dlt_arguments.append(child_value)

        # Parse length
        child = ARObject._find_child_element(element, "LENGTH")
        if child is not None:
            length_value = child.text
            obj.length = length_value

        # Parse network
        child = ARObject._find_child_element(element, "NETWORK")
        if child is not None:
            network_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.network = network_value

        # Parse optional
        child = ARObject._find_child_element(element, "OPTIONAL")
        if child is not None:
            optional_value = child.text
            obj.optional = optional_value

        # Parse predefined_text
        child = ARObject._find_child_element(element, "PREDEFINED-TEXT")
        if child is not None:
            predefined_text_value = child.text
            obj.predefined_text = predefined_text_value

        # Parse variable_length
        child = ARObject._find_child_element(element, "VARIABLE-LENGTH")
        if child is not None:
            variable_length_value = child.text
            obj.variable_length = variable_length_value

        return obj



class DltArgumentBuilder:
    """Builder for DltArgument."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltArgument = DltArgument()

    def build(self) -> DltArgument:
        """Build and return DltArgument object.

        Returns:
            DltArgument instance
        """
        # TODO: Add validation
        return self._obj

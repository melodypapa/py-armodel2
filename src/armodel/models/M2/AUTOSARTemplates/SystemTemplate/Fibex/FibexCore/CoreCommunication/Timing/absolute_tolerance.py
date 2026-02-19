"""AbsoluteTolerance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 398)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class AbsoluteTolerance(ARObject):
    """AUTOSAR AbsoluteTolerance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    absolute: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize AbsoluteTolerance."""
        super().__init__()
        self.absolute: Optional[TimeValue] = None
    def serialize(self) -> ET.Element:
        """Serialize AbsoluteTolerance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize absolute
        if self.absolute is not None:
            serialized = ARObject._serialize_item(self.absolute, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ABSOLUTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbsoluteTolerance":
        """Deserialize XML element to AbsoluteTolerance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbsoluteTolerance object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse absolute
        child = ARObject._find_child_element(element, "ABSOLUTE")
        if child is not None:
            absolute_value = child.text
            obj.absolute = absolute_value

        return obj



class AbsoluteToleranceBuilder:
    """Builder for AbsoluteTolerance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbsoluteTolerance = AbsoluteTolerance()

    def build(self) -> AbsoluteTolerance:
        """Build and return AbsoluteTolerance object.

        Returns:
            AbsoluteTolerance instance
        """
        # TODO: Add validation
        return self._obj

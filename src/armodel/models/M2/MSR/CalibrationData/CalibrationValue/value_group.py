"""ValueGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 458)

JSON Source: docs/json/packages/M2_MSR_CalibrationData_CalibrationValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_values import (
        SwValues,
    )



class ValueGroup(ARObject):
    """AUTOSAR ValueGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    label: Optional[MultilanguageLongName]
    vg_contents: Optional[SwValues]
    def __init__(self) -> None:
        """Initialize ValueGroup."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.vg_contents: Optional[SwValues] = None

    def serialize(self) -> ET.Element:
        """Serialize ValueGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize label
        if self.label is not None:
            serialized = ARObject._serialize_item(self.label, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vg_contents
        if self.vg_contents is not None:
            serialized = ARObject._serialize_item(self.vg_contents, "SwValues")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VG-CONTENTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ValueGroup":
        """Deserialize XML element to ValueGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ValueGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse label
        child = ARObject._find_child_element(element, "LABEL")
        if child is not None:
            label_value = ARObject._deserialize_by_tag(child, "MultilanguageLongName")
            obj.label = label_value

        # Parse vg_contents
        child = ARObject._find_child_element(element, "VG-CONTENTS")
        if child is not None:
            vg_contents_value = ARObject._deserialize_by_tag(child, "SwValues")
            obj.vg_contents = vg_contents_value

        return obj



class ValueGroupBuilder:
    """Builder for ValueGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ValueGroup = ValueGroup()

    def build(self) -> ValueGroup:
        """Build and return ValueGroup object.

        Returns:
            ValueGroup instance
        """
        # TODO: Add validation
        return self._obj

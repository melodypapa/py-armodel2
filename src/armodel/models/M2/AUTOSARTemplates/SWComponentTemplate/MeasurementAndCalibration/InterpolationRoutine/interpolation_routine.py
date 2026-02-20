"""InterpolationRoutine AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 430)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 46)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_MeasurementAndCalibration_InterpolationRoutine.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class InterpolationRoutine(ARObject):
    """AUTOSAR InterpolationRoutine."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    interpolation_ref: Optional[ARRef]
    is_default: Optional[Boolean]
    short_label: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize InterpolationRoutine."""
        super().__init__()
        self.interpolation_ref: Optional[ARRef] = None
        self.is_default: Optional[Boolean] = None
        self.short_label: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize InterpolationRoutine to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize interpolation_ref
        if self.interpolation_ref is not None:
            serialized = ARObject._serialize_item(self.interpolation_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERPOLATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_default
        if self.is_default is not None:
            serialized = ARObject._serialize_item(self.is_default, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = ARObject._serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InterpolationRoutine":
        """Deserialize XML element to InterpolationRoutine object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InterpolationRoutine object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse interpolation_ref
        child = ARObject._find_child_element(element, "INTERPOLATION-REF")
        if child is not None:
            interpolation_ref_value = ARRef.deserialize(child)
            obj.interpolation_ref = interpolation_ref_value

        # Parse is_default
        child = ARObject._find_child_element(element, "IS-DEFAULT")
        if child is not None:
            is_default_value = child.text
            obj.is_default = is_default_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        return obj



class InterpolationRoutineBuilder:
    """Builder for InterpolationRoutine."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InterpolationRoutine = InterpolationRoutine()

    def build(self) -> InterpolationRoutine:
        """Build and return InterpolationRoutine object.

        Returns:
            InterpolationRoutine instance
        """
        # TODO: Add validation
        return self._obj

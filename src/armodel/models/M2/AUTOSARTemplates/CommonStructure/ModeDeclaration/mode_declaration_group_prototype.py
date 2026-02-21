"""ModeDeclarationGroupPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 42)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 113)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2038)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 233)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwCalibrationAccessEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeDeclarationGroupPrototype(Identifiable):
    """AUTOSAR ModeDeclarationGroupPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_calibration_access: Optional[SwCalibrationAccessEnum]
    type_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeDeclarationGroupPrototype."""
        super().__init__()
        self.sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
        self.type_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeDeclarationGroupPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeDeclarationGroupPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_calibration_access
        if self.sw_calibration_access is not None:
            serialized = SerializationHelper.serialize_item(self.sw_calibration_access, "SwCalibrationAccessEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-CALIBRATION-ACCESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type_ref
        if self.type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.type_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationGroupPrototype":
        """Deserialize XML element to ModeDeclarationGroupPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeDeclarationGroupPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeDeclarationGroupPrototype, cls).deserialize(element)

        # Parse sw_calibration_access
        child = SerializationHelper.find_child_element(element, "SW-CALIBRATION-ACCESS")
        if child is not None:
            sw_calibration_access_value = SwCalibrationAccessEnum.deserialize(child)
            obj.sw_calibration_access = sw_calibration_access_value

        # Parse type_ref
        child = SerializationHelper.find_child_element(element, "TYPE-REF")
        if child is not None:
            type_ref_value = ARRef.deserialize(child)
            obj.type_ref = type_ref_value

        return obj



class ModeDeclarationGroupPrototypeBuilder:
    """Builder for ModeDeclarationGroupPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationGroupPrototype = ModeDeclarationGroupPrototype()

    def build(self) -> ModeDeclarationGroupPrototype:
        """Build and return ModeDeclarationGroupPrototype object.

        Returns:
            ModeDeclarationGroupPrototype instance
        """
        # TODO: Add validation
        return self._obj

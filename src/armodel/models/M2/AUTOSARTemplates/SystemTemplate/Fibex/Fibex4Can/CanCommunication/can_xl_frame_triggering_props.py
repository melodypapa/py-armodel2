"""CanXlFrameTriggeringProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2007)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanXlFrameTriggeringProps(ARObject):
    """AUTOSAR CanXlFrameTriggeringProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    acceptance_field: Optional[PositiveInteger]
    priority_id: Optional[PositiveInteger]
    sdu_type: Optional[PositiveInteger]
    vcid: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CanXlFrameTriggeringProps."""
        super().__init__()
        self.acceptance_field: Optional[PositiveInteger] = None
        self.priority_id: Optional[PositiveInteger] = None
        self.sdu_type: Optional[PositiveInteger] = None
        self.vcid: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanXlFrameTriggeringProps":
        """Deserialize XML element to CanXlFrameTriggeringProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanXlFrameTriggeringProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse acceptance_field
        child = ARObject._find_child_element(element, "ACCEPTANCE-FIELD")
        if child is not None:
            acceptance_field_value = child.text
            obj.acceptance_field = acceptance_field_value

        # Parse priority_id
        child = ARObject._find_child_element(element, "PRIORITY-ID")
        if child is not None:
            priority_id_value = child.text
            obj.priority_id = priority_id_value

        # Parse sdu_type
        child = ARObject._find_child_element(element, "SDU-TYPE")
        if child is not None:
            sdu_type_value = child.text
            obj.sdu_type = sdu_type_value

        # Parse vcid
        child = ARObject._find_child_element(element, "VCID")
        if child is not None:
            vcid_value = child.text
            obj.vcid = vcid_value

        return obj



class CanXlFrameTriggeringPropsBuilder:
    """Builder for CanXlFrameTriggeringProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanXlFrameTriggeringProps = CanXlFrameTriggeringProps()

    def build(self) -> CanXlFrameTriggeringProps:
        """Build and return CanXlFrameTriggeringProps object.

        Returns:
            CanXlFrameTriggeringProps instance
        """
        # TODO: Add validation
        return self._obj

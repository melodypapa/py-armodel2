"""BuildEngineeringObject AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 372)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
    EngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RegularExpression,
    UriString,
)


class BuildEngineeringObject(EngineeringObject):
    """AUTOSAR BuildEngineeringObject."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    file_type: NameToken
    file_type_pattern: RegularExpression
    intended: Optional[UriString]
    def __init__(self) -> None:
        """Initialize BuildEngineeringObject."""
        super().__init__()
        self.file_type: NameToken = None
        self.file_type_pattern: RegularExpression = None
        self.intended: Optional[UriString] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildEngineeringObject":
        """Deserialize XML element to BuildEngineeringObject object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildEngineeringObject object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse file_type
        child = ARObject._find_child_element(element, "FILE-TYPE")
        if child is not None:
            file_type_value = child.text
            obj.file_type = file_type_value

        # Parse file_type_pattern
        child = ARObject._find_child_element(element, "FILE-TYPE-PATTERN")
        if child is not None:
            file_type_pattern_value = child.text
            obj.file_type_pattern = file_type_pattern_value

        # Parse intended
        child = ARObject._find_child_element(element, "INTENDED")
        if child is not None:
            intended_value = child.text
            obj.intended = intended_value

        return obj



class BuildEngineeringObjectBuilder:
    """Builder for BuildEngineeringObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildEngineeringObject = BuildEngineeringObject()

    def build(self) -> BuildEngineeringObject:
        """Build and return BuildEngineeringObject object.

        Returns:
            BuildEngineeringObject instance
        """
        # TODO: Add validation
        return self._obj

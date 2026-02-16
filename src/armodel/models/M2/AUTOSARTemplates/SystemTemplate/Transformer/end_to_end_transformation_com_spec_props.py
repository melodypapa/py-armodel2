"""EndToEndTransformationComSpecProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import (
    TransformationComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.e2_e_profile_compatibility_props import (
    E2EProfileCompatibilityProps,
)


class EndToEndTransformationComSpecProps(TransformationComSpecProps):
    """AUTOSAR EndToEndTransformationComSpecProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("clear_from_valid", None, True, False, None),  # clearFromValid
        ("disable_end_to", None, True, False, None),  # disableEndTo
        ("e2e_profile", None, False, False, E2EProfileCompatibilityProps),  # e2eProfile
        ("max_delta", None, True, False, None),  # maxDelta
        ("max_error_state", None, True, False, None),  # maxErrorState
        ("max_no_new_or", None, True, False, None),  # maxNoNewOr
        ("min_ok_state_init", None, True, False, None),  # minOkStateInit
        ("min_ok_state", None, True, False, None),  # minOkState
        ("sync_counter_init", None, True, False, None),  # syncCounterInit
        ("window_size_init", None, True, False, None),  # windowSizeInit
        ("window_size", None, True, False, None),  # windowSize
    ]

    def __init__(self) -> None:
        """Initialize EndToEndTransformationComSpecProps."""
        super().__init__()
        self.clear_from_valid: Optional[Boolean] = None
        self.disable_end_to: Optional[Boolean] = None
        self.e2e_profile: Optional[E2EProfileCompatibilityProps] = None
        self.max_delta: Optional[PositiveInteger] = None
        self.max_error_state: Optional[PositiveInteger] = None
        self.max_no_new_or: Optional[PositiveInteger] = None
        self.min_ok_state_init: Optional[PositiveInteger] = None
        self.min_ok_state: Optional[PositiveInteger] = None
        self.sync_counter_init: Optional[PositiveInteger] = None
        self.window_size_init: Optional[PositiveInteger] = None
        self.window_size: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EndToEndTransformationComSpecProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndTransformationComSpecProps":
        """Create EndToEndTransformationComSpecProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EndToEndTransformationComSpecProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EndToEndTransformationComSpecProps since parent returns ARObject
        return cast("EndToEndTransformationComSpecProps", obj)


class EndToEndTransformationComSpecPropsBuilder:
    """Builder for EndToEndTransformationComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndTransformationComSpecProps = EndToEndTransformationComSpecProps()

    def build(self) -> EndToEndTransformationComSpecProps:
        """Build and return EndToEndTransformationComSpecProps object.

        Returns:
            EndToEndTransformationComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
